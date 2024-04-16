import asyncio
import time
import random

mailbox = False
start = time.perf_counter()
counter = 0

print("Starting...")

async def monitor_mailbox():
    global mailbox
    global counter

    while True:
        print(f"Mailbox status: {mailbox}, Counter: {counter}")

        if mailbox:
            print(f"MONITOR: got the mailbox at: {time.perf_counter() - start:.2f}")
            mailbox = False
            counter += 1

            if counter > 5:  # Optional: stopping condition
                print("Counter reached 5, stopping...")
                break
        else:
            rand = random.randint(1, 3)
            print(f"MONITOR: waiting {rand} seconds at {time.perf_counter() - start:.2f}")
            await asyncio.sleep(rand)

async def mailman():
    global mailbox

    while True:
        if random.randint(0, 10) > 5 and not mailbox:
            mailbox = True
            print(f"MAILMAN: put something in the mailbox at {time.perf_counter() - start:.2f}")
        else:
            rand = random.randint(3, 5)
            print(f"MAILMAN: waiting {rand} seconds at {time.perf_counter() - start:.2f}")
            await asyncio.sleep(rand)

async def main():
    task1 = asyncio.create_task(monitor_mailbox())
    task2 = asyncio.create_task(mailman())

    # Wait for both tasks to complete (this will effectively wait forever unless you break the loop within the tasks)
    await task1
    await task2

# Run the main function using asyncio.run if this is the main module
if __name__ == "__main__":
    asyncio.run(main())
