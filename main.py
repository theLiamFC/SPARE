import openAI_assistant
import openAIAlchemy

### ByteBard_XML ID
bb_id = "asst_CFsqmgnJhalDKnZvyjGKOtg7"
### PrimeBot ID
pb_id = "asst_merTUbrMxt0Fo1sc9P17G1Ax"

### General test thread
# thread_id = "thread_UbU1hougFO6WE4kJCmK0ylRR"

# response = openAI_assistant.callChad(
#     bb_id, thread_id, "what is the weather in lexington MA"
# )


AI_interface = openAIAlchemy(bb_id, debug=True)
repsonse = AI_interface.run("what is the weather in lexington MA")
print(repsonse)


def send_to_serial():
    pass
