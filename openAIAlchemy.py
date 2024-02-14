from openai import OpenAI
import time
import asyncio

# assistant_id
# thread_id
# clien


class openAIAlchemy:
    def __init__(self, assistant_id, thread_id=None, debug=False):
        self.client = OpenAI()
        self.debug = debug

        if thread_id == None:
            newThread = self.client.beta.threads.create()
            self.threadID = newThread.id
            if self.debug:
                print("THREAD_ID: ", self.threadID)
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

    # add message from help desk or human input
    # how do we distinguish function responses?
    def addMessage(self, message):
        self.client.beta.threads.messages.create(
            self.thread_id,
            role="user",
            content=message,
        )

    # must parse between user, assistant, function
    def getMessage(self):
        messages = self.client.beta.threads.messages.list(self.thread_id)

        # get role of most recent message
        messages.data[0].role

        # get content of most recent message
        messages.data[0].content[0].text.value

    # must begin new run whenever a message is added to the thread
    async def __runManager(self):
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread_id, assistant_id=self.assistant_id
        )
        status = "in_progress"
        while status != "completed" and status != "failed":
            status = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread_id, run_id=run.id
            ).status
            await asyncio.sleep(100)
        if status == "failed":
            # throw exception
            print("Run Failed")
            print(
                self.client.beta.threads.runs.retrieve(
                    thread_id=self.thread_id, run_id=run.id
                )
            )

    # Public method to start the OpenAI run asynchronously
    def run(self, message):
        if self.debug:
            print("running message")
        # First, add the message to the thread
        self.addMessage(message)
        # Then, run the asynchronous method using asyncio
        asyncio.run(self.__runManager())
