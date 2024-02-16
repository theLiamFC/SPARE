from openai import OpenAI
import time
import asyncio
import json

#### private variables
# assistant_id
# thread_id
# client_id
# debug


class openAIAlchemy:
    def __init__(self, assistant_id, thread_id=None, debug=False):
        self.client = OpenAI()
        self.debug = debug

        if thread_id == None:
            newThread = self.client.beta.threads.create()
            self.thread_id = newThread.id
            if self.debug:
                print("THREAD_ID: ", self.thread_id)
        else:
            self.thread_id = thread_id

        self.assistant_id = assistant_id

    # Public Debugging Function
    # Retreive assistants for purpose of finding IDs
    def getAssistants(self):
        my_assistants = self.client.beta.assistants.list(
            order="desc",
            limit="20",
        )
        return my_assistants.data

    # Public Debugging Function
    # Retrieve runs in a given thread
    def getRuns(self):
        runs = self.client.beta.threads.runs.list(self.thread_id)
        return runs

    def killAllRuns(self):
        runs = self.getRuns()
        for run in runs.data:
            if run.status == "in_progress" or run.status == "requires_action":
                self.client.beta.threads.runs.cancel(
                    thread_id=self.thread_id, run_id=run.id
                )

    # add message from help desk or human input
    # how do we distinguish function responses?
    def addMessage(self, message):
        if self.debug:
            print("Adding Message")
        self.client.beta.threads.messages.create(
            self.thread_id,
            role="user",
            content=message,
        )
        self.__runManager()

    # must parse between user, assistant, function
    def getMessage(self):
        messages = self.client.beta.threads.messages.list(self.thread_id)

        # get role of most recent message
        if messages.data[0].role == "function":
            # call function to deal with functions
            pass

        # get content of most recent message
        return messages.data[0].content[0].text.value

    async def __runManager(self):
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread_id, assistant_id=self.assistant_id
        )

        if self.debug:
            print("Run in progress")
        status = "in_progress"
        
        # non asyncio version
        while status not in ["completed", "failed","requires_action]:
            status = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread_id, run_id=run.id
            ).status
            time.sleep(0.01)
        if status == "requires_action":
            calls = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread_id, run_id=run.id
            ).required_action
            self.__functionManager(calls)
        if status == "failed":
            # throw exception
            print("Run Failed")
            print(
                self.client.beta.threads.runs.retrieve(
                    thread_id=self.thread_id, run_id=run.id
                )
        # Asyncio version
        while status not in ["completed", "failed"]:
            run_details = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread_id, run_id=run.id
            )
            status = run_details.status
            print(status)
            await asyncio.sleep(1)  # Use asyncio.sleep for async code
        if status == "completed":
            # Assuming run_details contains a 'result' attribute with the data you need
            return self.client.beta.threads.messages.list(self.thread_id).data[0].content[0].text.value  # Return the actual result here
        elif status == "failed":
            # Handle failure, possibly returning an error message or details
            return "Run failed"

    def __functionManager(self, calls):
        for toolCall in calls.submit_tool_outputs.tool_calls:
            name = toolCall.function.name
            args = toolCall.function.arguments
            if name == "get_feedback":
                # print arg to command line and get written feedback
                pass
            elif name == "get_documentation":
                # search database for term and subsequent documentation
                pass
        print(calls.submit_tool_outputs.tool_calls)

    # Public method to start the OpenAI run asynchronously
    # def run(self, message):
    #     if self.debug:
    #         print("running message")
    #     # First, add the message to the thread
    #     self.addMessage(message)
    #     # Then, run the asynchronous method using asyncio
    #     asyncio.run(self.__runManager())
    async def run(self, message):
        if self.debug:
            print("running message")
        self.addMessage(message)
        result = await self.__runManager()  # Await the result from __runManager
        return result  # Return the
