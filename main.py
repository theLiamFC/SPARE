from ai_alchemy import AIAlchemy
import asyncio
import sys
import json
import time
import nest_asyncio
nest_asyncio.apply()
### AI Alchemist Assistant ID - this is NOT an API key
# SPIKE_ID = "asst_8WN5ksXpnNaBeAr1IKrLq4yd"
# WORKER_ID = "asst_gCp1YejKuc6X1progQ99C2fL"
default_messages = {
    "0": "Move the spike prime forwards in a loop. There are motors in ports A and B",
    "1": "Move forward and backwards in order to maintin a distance of 100 using distance senor in port D and motors in ports A and B",
    "2": "Create a theramin using a touch sensor in port C and a distance sensor in port F",
    "3": "Print hello world to terminal: print('hello world')",
    "4": "Make a blue line following robot. There are motors in ports A and B and a color sensor in port C",
    "5": "Make roomba like robot that moves forwards until it hits something with the touch sensor \
and then it backs up, turns and moves forwards again. There are motors in ports A and B and a force senor in port F",
    "6": "I am placing the robot on a seesaw platform, balance at the center of the platform",
}


# Main interface loop
async def interface_loop(ceo_assistant):
    intro_statement = "ChatGPT: What would you like to code today?\n"
    input_statement = (
        "['e','exit'] to stop the program.\n['help'] to see example prompts\n\nHuman: "
    )

    # Clear terminal screen
    for i in range(20):
        print("\n")
    user_prompt = input(intro_statement + input_statement)
    print()

    # Begin interface loop
    while True:
        if user_prompt.lower() == "help":
            print(str(json.dumps(default_messages, indent=4)) + "\n")
            user_prompt = input(input_statement)
            continue

        if user_prompt.lower() == "e" or user_prompt.lower() == "exit":
            print("Exiting the program...")
            return

        if user_prompt in default_messages:
            user_prompt = default_messages[user_prompt]
            print(f"Using default message: {user_prompt}\n")

        # Call ChatGPT with prompt
        result = await ceo_assistant.run_thread(user_prompt)
        print("ChatGPT: " + result)

        user_prompt = input(input_statement)
        print()

async def run_assistant(ceo_assistant,tg):
    result = await ceo_assistant.run(tg)
    return result

async def check_mailbox(ceo_assistant):
    while True:
        if ceo_assistant.out_mail != None:
            print(f"mcm - {ceo_assistant.name} -> {user_name}: {ceo_assistant.out_mail}")
            ceo_assistant.out_mail = None
            user_prompt = input(f"mcminput - {user_name} ->  {ceo_assistant.name}: ")
            
            ceo_assistant.in_mail = user_prompt

        else:
            await asyncio.sleep(1)

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(check_mailbox(ceo_assistant))
        task2 = tg.create_task(run_assistant(ceo_assistant, tg)) # pass TG through

if __name__ == "__main__":
    
    # Clear terminal screen
    for i in range(20):
        print("\n")

    #### CHANGE SERIAL PORT HERE ####
    serial_port = "/dev/cu.usbmodem3356396133381"
    device = "SPIKE"
    role = "ceo"
    name = "CEO"

    user_name = input("Hi! Whats your name? ")
    intro_statement = f"{name}: What would you like to code today?\n"
    input_statement = (
        f"['e','exit'] to stop the program.\n['help'] to see example prompts\n"
    )

    user_prompt = input(intro_statement + input_statement + f"{user_name} ->  {name}: ")
    print()

    # Instantiate AIAlchemy Class
    task = f"{default_messages['0']} use serial port /dev/cu.usbmodem3356396133381"
    device = "SPIKE"
    role = "ceo"
    name = "CEO"
    ceo_assistant = AIAlchemy(name, role, task, user_name, debug=False, verbose=False)

    asyncio.run(main())

    # start loop
    # fred = asyncio.new_event_loop()
    # fred.create_task(check_mailbox(ceo_assistant))
    # fred.create_task(run_assistant(ceo_assistant))
    # fred.run_forever()
    
    # asyncio.run(check_mailbox(ceo_assistant))
    # asyncio.run(run_assistant(ceo_assistant))

    # task1 = asyncio.create_task(run_assistant(ceo_assistant))
    # task2 = asyncio.create_task(check_mailbox(ceo_assistant))

    # # Wait for both tasks to complete (this will effectively wait forever unless you break the loop within the tasks)
    # asyncio.gather(task1, task2)

    time.sleep(100)
    sys.exit()
    # Initiate Main Loop
    try:
        asyncio.run(interface_loop(ceo_assistant))
    except Exception as e:
        print("Main Loop Error: ", e)
    finally:
        ceo_assistant.close()
 