from openai import OpenAI
import time
import asyncio

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

    def killRun(self, run_id):
        self.client.beta.threads.runs.cancel(thread_id=self.thread_id, run_id=run_id)

    # add message from help desk or human input
    # how do we distinguish function responses?
    def addMessage(self, message):
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
        messages.data[0].role

        # get content of most recent message
        return messages.data[0].content[0].text.value

    async def __runManager(self):
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread_id, assistant_id=self.assistant_id
        )

        if self.debug:
            print("Run in progress")
        status = "in_progress"
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

    async def run(self, message):
        if self.debug:
            print("running message")
        self.addMessage(message)
        result = await self.__runManager()  # Await the result from __runManager
        return result  # Return the