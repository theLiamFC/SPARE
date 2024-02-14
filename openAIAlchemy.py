from openai import OpenAI
import time
import asyncio


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

    # Make a call to specific ChatGPT assistant
    # Returns response
    # BUG Should make asynchronous in the future
    def callChad(self, assistantID, threadID, prompt):
        self.client.beta.threads.messages.create(
            threadID,
            role="user",
            content=prompt,
        )
        run = self.client.beta.threads.runs.create(
            thread_id=threadID, assistant_id=assistantID
        )
        status = "in_progress"
        while status != "completed" and status != "failed":
            time.sleep(0.5)
            status = self.client.beta.threads.runs.retrieve(
                thread_id=threadID, run_id=run.id
            ).status
        return (
            self.client.beta.threads.messages.list(threadID)
            .data[0]
            .content[0]
            .text.value
        )
