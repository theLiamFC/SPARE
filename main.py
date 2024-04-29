from ai_alchemy import AIAlchemy
import asyncio
import sys
import json
import time
import nest_asyncio
nest_asyncio.apply()
import tkinter

### AI Alchemist Assistant ID - this is NOT an API key
# SPIKE_ID = "asst_8WN5ksXpnNaBeAr1IKrLq4yd"
# WORKER_ID = "asst_gCp1YejKuc6X1progQ99C2fL"
serial_1 = "/dev/cu.usbmodem3356396133381"
serial_2 = "/dev/tty.usbmodem3844343A31371" # liam's
serial_2 = "/dev/tty.usbmodem14301" # jesse's
serial_3 = serial_2
default_messages = {
    "0": f"Move the spike prime forwards. There are motors in ports A and B. Use serial port {serial_1}",
    "1": f"Move forward and backwards in order to maintin a distance of 100 using distance senor in port D and motors in ports A and B",
    "2": f"Create a theramin using a touch sensor in port C and a distance sensor in port F",
    "3": f"Print hello world to terminal: print('hello world')",
    "4": f"Make a blue line following robot. There are motors in ports A and B and a color sensor in port C",
    "5": f"Make roomba like robot that moves forwards until it hits something with the touch sensor \
and then it backs up, turns and moves forwards again. There are motors in ports A and B and a force senor in port F",
    "6": f"I am placing the robot on a seesaw platform, balance at the center of the platform",
    "7": f"I have two micropython microcontrollers connected over serial. A SPIKE in Port {serial_1} (which has motors in ports A and B) and an OpenMV camera in Port {serial_2}. I want to you make the SPIKE wave a motor when the OpenMV camera sees a face.",
    "8": f"I have two micropython microcontrollers connected over serial. A SPIKE in Port {serial_1} (which has motors in ports A and B) and a Raspberry Pi Pico in Port {serial_2}. I want to you make the SPIKE wave a motor when Pin 11 on the Pico goes high.",
    "9": f"I have three micropython microcontrollers connected over serial. A SPIKE in Port {serial_1} (which has motors in ports A and B), a Raspberry Pi Pico in Port {serial_2}, and an OpenMV cameria in Port {serial_3}. I want to you make the SPIKE wave a motor when the OpenMV camera sees a face, which will send a high signal of pin 11 to the pic owhich will then send a bluetooth signal to the SPIKE.",
}


async def run_assistant(ceo_assistant,tg):
    result = await ceo_assistant.run(tg)
    return result

async def check_mailbox(ceo_assistant):
    intro_statement = f"{name}: What would you like to code today?\n"
    input_statement = (
        f"['e','exit'] to stop the program.\n['help'] to see example prompts\n"
    )
    print(intro_statement)
    print(input_statement)
    while True:
        if ceo_assistant.out_mail != None:
            print(f"{ceo_assistant.name}: {ceo_assistant.out_mail}\n")
            ceo_assistant.out_mail = None
            user_prompt = input(f"{user_name}: ")
            print()
            if user_prompt == "e" or user_prompt == "exit":
                await ceo_assistant.close()
                return
            elif user_prompt == "help":
                print(default_messages)
                pass
            elif user_prompt in default_messages:
                user_prompt = default_messages[user_prompt]
            
            ceo_assistant.log_print(user_prompt)
            ceo_assistant.in_mail = user_prompt

        else:
            await asyncio.sleep(1)

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(check_mailbox(ceo_assistant))
        task2 = tg.create_task(run_assistant(ceo_assistant, tg)) # pass TG through

if __name__ == "__main__":

    # import os
    # os.system("python log_printing_gui.py")
    import subprocess
    # call(["python", "log_printing_gui.py"])
    subprocess.Popen(["python", "log_printing_gui.py"])


    # Clear terminal screen
    for i in range(20):
        print("\n")

    #### CHANGE SERIAL PORT HERE ####
    serial_port = "/dev/cu.usbmodem3356396133381"
    device = "SPIKE"
    role = "ceo"
    name = "CEO"

    user_name = "JESSE"
    # user_name = input("Hi! Whats your name? ")

    intro_statement = f"{name}: What would you like to code today?\n"
    input_statement = (
        f"['e','exit'] to stop the program.\n['help'] to see example prompts\n"
    )

    # Instantiate AIAlchemy Class
    device = "SPIKE"
    role = "ceo"
    name = "CEO"
    ceo_assistant = AIAlchemy(name, role, user_name, debug=False, verbose=False)

    asyncio.run(main())

    time.sleep(100)
    sys.exit()
    # Initiate Main Loop
    # try:
    #     asyncio.run(interface_loop(ceo_assistant))
    # except Exception as e:
    #     print("Main Loop Error: ", e)
    # finally:
    #     ceo_assistant.close()
