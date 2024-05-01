from ai_alchemy import AIAlchemy
# from ai_alchemy import default_messages
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

async def run_assistant(manager_assistant,tg):
    result = await manager_assistant.run(tg)
    return result

async def check_mailbox(manager_assistant):
    # intro_statement = f"{name}: What would you like to code today?\n"
    # input_statement = (
    #     f"['e','exit'] to stop the program.\n['help'] to see example prompts\n"
    # )
    # print(intro_statement)
    # print(input_statement)
    while True:
        if manager_assistant.out_mail != None:
            print(f"{manager_assistant.name}: {manager_assistant.out_mail}\n")
            manager_assistant.out_mail = None
            user_prompt = input(f"{user_name}: ")
            print()
            # if user_prompt == "e" or user_prompt == "exit":
            #     await manager_assistant.close()
            #     return
            # elif user_prompt == "help":
            #     print(default_messages)
            #     pass
            # elif user_prompt in default_messages:
            #     user_prompt = default_messages[user_prompt]
            
            manager_assistant.log_print(user_prompt)
            manager_assistant.in_mail = user_prompt

        else:
            await asyncio.sleep(1)

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(check_mailbox(manager_assistant))
        task2 = tg.create_task(run_assistant(manager_assistant, tg)) # pass TG through

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
    role = "manager"
    name = "MANAGER"

    user_name = "JESSE"
    # user_name = input("Hi! Whats your name? ")

    # Instantiate AIAlchemy Class
    device = "SPIKE"
    role = "manager"
    name = "MANAGER"
    manager_assistant = AIAlchemy(name, role, user_name, debug=False, verbose=False)

    asyncio.run(main())

    time.sleep(100)
    sys.exit()
    # Initiate Main Loop
    # try:
    #     asyncio.run(interface_loop(manager_assistant))
    # except Exception as e:
    #     print("Main Loop Error: ", e)
    # finally:
    #     manager_assistant.close()
