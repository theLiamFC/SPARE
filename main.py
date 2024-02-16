import openAI_assistant
from openAIAlchemy import openAIAlchemy
import serial_interface
import asyncio
import sys

### ByteBard_XML ID
bb_id = "asst_CFsqmgnJhalDKnZvyjGKOtg7"
### PrimeBot ID
pb_id = "asst_merTUbrMxt0Fo1sc9P17G1Ax"
### Arduino Alvik ID
aa_id = "asst_NiIdeWySoj4RYIRU7t6r2mpG"

### General test thread
# thread_id = "thread_UbU1hougFO6WE4kJCmK0ylRR"

# response = openAI_assistant.callChad(
#     bb_id, thread_id, "what is the weather in lexington MA"
# )


# AI_interface = openAIAlchemy(bb_id, debug=True)
# response = AI_interface.run("code the robot to move straight forward")
# print(response)



### TESTING SERIAL
test = ''''
print("hello world")
'''
serial_interface.serial_write(bytes(test, 'utf-8'))
print(serial_interface.serial_read())

sys.exit()
##############################

def extract_code(result):
    idx1 = result.find("```") + 3 + 6
    idx2 = result[idx1:].find("```") + idx1
    code = result[idx1:idx2]
    return code


async def main():
    # Assuming `instance` is an instance of the class containing your run method
    AI_interface = openAIAlchemy(aa_id, debug=True)

    result = await AI_interface.run("write code to move the bot forward")
    code = extract_code(result)
    serial_interface.serial_write(bytes(code, 'utf-8'))


# Run the main function in the event loop
if __name__ == "__main__":
    asyncio.run(main())
