from openai import OpenAI
import time


class openAIAlchemy:
    def __init__():
        client = OpenAI()

    # Retreive assistants for purpose of finding IDs
    def getAssistants(self):
        my_assistants = self.client.beta.assistants.list(
            order="desc",
            limit="20",
        )
        return my_assistants.data

    # Retrieve runs in a given thread
    def getRuns(self, thread_id):
        runs = self.client.beta.threads.runs.list(thread_id)
        return runs

    # edit
