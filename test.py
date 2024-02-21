import openAIAlchemy

### ByteBard_XML ID
bb_id = "asst_CFsqmgnJhalDKnZvyjGKOtg7"
### PrimeBot ID
pb_id = "asst_merTUbrMxt0Fo1sc9P17G1Ax"
### Ai Alchemist ID
aa_id = "asst_8WN5ksXpnNaBeAr1IKrLq4yd"

### General test thread
thread_id = "thread_UbU1hougFO6WE4kJCmK0ylRR"

# response = openAI_assistant.callChad(
#     bb_id, thread_id, "what is the weather in lexington MA"
# )


AI_interface = openAIAlchemy.openAIAlchemy(
    aa_id, thread_id="thread_1GwlxP7aLrP4rQXnM2qyQmhY", debug=True
)
AI_interface.killAllRuns()
# # print(AI_interface.getRuns())

AI_interface.addMessage(
    "write code that will drive a car and move around obstacles using an ultrasonic sensor. make sure to check with a human to ensure the car is driving correctly"
)
print(AI_interface.getMessage())
