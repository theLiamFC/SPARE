import openAIAlchemy

### ByteBard_XML ID
bb_id = "asst_CFsqmgnJhalDKnZvyjGKOtg7"
### PrimeBot ID
pb_id = "asst_merTUbrMxt0Fo1sc9P17G1Ax"

### General test thread
thread_id = "thread_UbU1hougFO6WE4kJCmK0ylRR"

# response = openAI_assistant.callChad(
#     bb_id, thread_id, "what is the weather in lexington MA"
# )


AI_interface = openAIAlchemy.openAIAlchemy(
    bb_id, thread_id="thread_1GwlxP7aLrP4rQXnM2qyQmhY", debug=True
)
# print(AI_interface.getRuns())
# AI_interface.killRun("run_hxxrB7mi7BDYs6464lWwXbdv")
AI_interface.addMessage("what is the weather in lexington MA")
print(AI_interface.getMessage())
