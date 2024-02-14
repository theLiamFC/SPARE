from openai import OpenAI
import json
import time

client = OpenAI()


# Retreive assistants for purpose of finding IDs
def getAssistants(client):
    my_assistants = client.beta.assistants.list(
        order="desc",
        limit="20",
    )
    return my_assistants.data


# Make a call to specific ChatGPT assistant
# Returns response
# BUG Should make asynchronous in the future
def callChad(assistantID, threadID, prompt):
    client.beta.threads.messages.create(
        threadID,
        role="user",
        content=prompt,
    )
    run = client.beta.threads.runs.create(thread_id=threadID, assistant_id=assistantID)
    status = "in_progress"
    temp = None
    while status != "completed" and status != "failed":
        time.sleep(0.5)
        status = client.beta.threads.runs.retrieve(
            thread_id=threadID, run_id=run.id
        ).status
        temp = client.beta.threads.runs.retrieve(thread_id=threadID, run_id=run.id)
    if status == "failed":
        print("Something went wrong")
        print(temp)
    return client.beta.threads.messages.list(threadID).data[0].content[0].text.value


### ByteBard_XML ID
bb_id = "asst_CFsqmgnJhalDKnZvyjGKOtg7"
### PrimeBot ID
pb_id = "asst_merTUbrMxt0Fo1sc9P17G1Ax"

### Create thread, do only once for each conversation.
# empty_thread = client.beta.threads.create()
# print(empty_thread.id)

### Test Thread ID
thread_id = "thread_UbU1hougFO6WE4kJCmK0ylRR"

### Create message within a thread
# thread_message = client.beta.threads.messages.create(
#     thread_id,
#     role="user",
#     content="How does AI work? Explain it in simple terms.",
# )
# print(thread_message)

# print(
#     callChad(
#         bb_id,
#         thread_id,
#         "write me a code for a spike prime with a color sensor in port A to detect the color blue.",
#     )
# )

# thread_messages = client.beta.threads.messages.list(thread_id)
# print(thread_messages.data[1].role)
