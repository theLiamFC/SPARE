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
### Ai Alchemist ID
aa_id = "asst_8WN5ksXpnNaBeAr1IKrLq4yd"

### General test thread
# thread_id = "thread_UbU1hougFO6WE4kJCmK0ylRR"

# response = openAI_assistant.callChad(
#     bb_id, thread_id, "what is the weather in lexington MA"
# )


async def interface_loop(ai_interface, serial_interface):
    # additional_instructions = "\nAdditional instructions: Make sure to run code before returning. \
    #     Use the get_visual_feedback function to confirm what the robot is doing"
    additional_instructions = "don't use the get_visul_feedback, just use get_feedback"
    user_prompt = input(
        "What would you like your spike prime to do today?\n[Enter 'e' or 'exit' to stop the program.]\n"
    )
    if user_prompt == "":
        user_prompt = ("Move forwards. There are motors in ports A and B")
        print(f"Using default message: {user_prompt}")
    elif user_prompt == "1":
        user_prompt = "Move forward and backwards in order to maintin a distance of 100 using distance senor in port D and motors in ports A and B"
        print(f"Using default message: {user_prompt}")
    elif user_prompt == "2":
        user_prompt = "Create a theramin.using a touch sensor in port C and a distance sensor in port F"
        print(f"Using default message: {user_prompt}")
    elif user_prompt == "3":
        user_prompt = "Print hello world to terminal: print('hello world')"
        print(f"Using default message: {user_prompt}")
    elif user_prompt == "4":
        user_prompt = "Make a blue line following robot. There are motors in ports A and B and a color sensor in port C"
        print(f"Using default message: {user_prompt}")

    while user_prompt.lower() != "e" and user_prompt.lower() != "exit":
        result = await ai_interface.run(user_prompt + additional_instructions)
        print(result)
        # code, response = ai_interface.extract_code(result)
        # print(response)
        # _reply = serial_interface.serial_write(bytes(code, 'utf-8'))
        user_prompt = input("[Enter 'e' or 'exit' to stop the program.]\n")


# Run the main function in the event loop
if __name__ == "__main__":
    port_l = "/dev/cu.usbmodem3356396133381"
    port_j = "COM13"
    
    serial = serial_interface.serial_interface(port_j)
    # serial.test_serial()

    ai_interface = openAIAlchemy(aa_id, serial, debug=False, verbose=False)
    try:
        asyncio.run(interface_loop(ai_interface, serial))
    except Exception as e:
        print(e)
    finally:
        ai_interface.close()
