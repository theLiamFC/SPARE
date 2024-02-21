from openai import OpenAI
import time
import asyncio
import json
import sys
import serial_interface

#### private variables
# assistant_id
# thread_id
# client_id
# run_id
# debug

### ACTION ITEMS
# - create functionality for a debug log exported as txt file
# - build out interface loop to communicate over multiple runs
# - integrate json file for automated documentation returns
# - expand json file with more SPIKE syntax

class openAIAlchemy:
    def __init__(self, assistant_id, thread_id=None, debug=False):
        self.client = OpenAI()
        self.debug = debug
        self.run_id = None
        #self.debugText # build out logging functionality and export to txt file

        if thread_id == None:
            newThread = self.client.beta.threads.create()
            self.thread_id = newThread.id
            if self.debug:
                print("THREAD_ID: ", self.thread_id)
        else:
            self.thread_id = thread_id

        self.assistant_id = assistant_id

    # Public Debugging Function
    # Retreive assistants for purpose of finding IDs
    def getAssistants(self):
        my_assistants = self.client.beta.assistants.list(
            order="desc",
            limit="20",
        )
        return my_assistants.data

    # Public Debugging Function
    # Retrieve runs in a given thread
    def getRuns(self):
        runs = self.client.beta.threads.runs.list(self.thread_id)
        return runs

    def killAllRuns(self):
        runs = self.getRuns()
        for run in runs.data:
            if run.status == "in_progress" or run.status == "requires_action":
                self.client.beta.threads.runs.cancel(
                    thread_id=self.thread_id, run_id=run.id
                )

    # add message from help desk or human input
    # how do we distinguish function responses?
    def addMessage(self, message):
        if self.debug:
            print("Adding Message")
        self.client.beta.threads.messages.create(
            self.thread_id,
            role="user",
            content=message,
        )
        # self.__runManager()

    # must parse between user, assistant, function
    def getMessage(self):
        messages = self.client.beta.threads.messages.list(self.thread_id)

        # get role of most recent message
        if messages.data[0].role == "function":
            # call function to deal with functions
            pass

        # get content of most recent message
        return messages.data[0].content[0].text.value

    async def __runManager(self):
        if self.run_id == None:
            if self.debug: print("Creating new run")
            run = self.client.beta.threads.runs.create(
                thread_id=self.thread_id, assistant_id=self.assistant_id
            )
            self.run_id = run.id
        else:
            if self.debug: print("Using existing run")
        if self.debug: print("Run in progress")
        status = "in_progress"
        
        # non asyncio version
        lastTime = time.time()
        while status not in ["completed", "failed","requires_action"]:
            status = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread_id, run_id=self.run_id
            ).status
            if self.debug and time.time() - lastTime > 5:
                print("Longer than normal runtime: ",status)
                lastTime = time.time()
            await asyncio.sleep(1)
        if self.debug: print("Status: " + status)
        if status == "requires_action":
            calls = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread_id, run_id=self.run_id
            ).required_action
            self.__functionManager(calls)
            return await self.__runManager()
        elif status == "completed":
            # Assuming run_details contains a 'result' attribute with the data you need
            self.run_id = None
            return self.client.beta.threads.messages.list(self.thread_id).data[0].content[0].text.value  # Return the actual result here
        elif status == "failed":
            # throw exception
            self.run_id = None
            print("Run Failed")
            print(
                self.client.beta.threads.runs.retrieve(
                    thread_id=self.thread_id, run_id=run.id
                ))

    def print_break(self, name, body):
        print("==================== " + name + " ====================")
        print(body)
        print("==================== " + "end" + " ====================")

    def __functionManager(self, calls):
        if self.debug: print("Managing functions")
        tool_outputs = []

        for toolCall in calls.submit_tool_outputs.tool_calls:
            # print(toolCall)
            id = toolCall.id
            # print(id)
            name = toolCall.function.name
            args = json.loads(toolCall.function.arguments)
            # case for every function available to assistant
            if name == "get_feedback":
                # print arg to command line and get written feedback
                print("Hey Human: ",args['prompt'])
                human_response = input()
                tool_outputs.append({
                    "tool_call_id": id,
                    "output": human_response,
                })
            elif name == "get_documentation":
                print("Query Dict: ",args['query'])
                query_response = input()
                tool_outputs.append({
                    "tool_call_id":id,
                    "output":query_response
                }) 
            elif name == "run_code":
                code = args['code']
                self.print_break("CODE", code)
                code = code.replace("\n", "\r\n")

                serial_response = serial_interface.serial_write(bytes(code, 'utf-8'))
                
                if self.debug: 
                    self.print_break("SERIAL OUTPUT", serial_response)
                tool_outputs.append({
                    "tool_call_id":id,
                    "output":serial_response
                }) 

        self.client.beta.threads.runs.submit_tool_outputs(
            thread_id = self.thread_id,
            run_id=self.run_id,
            tool_outputs=tool_outputs
        )


    def extract_code(self,  result):
        idx1 = result.find("```") + 3 + 7
        idx2 = result[idx1:].find("```") + idx1
        code = result[idx1:idx2]
        breaker  = "============ CODE ============\n"
        breaker1 = "==============================\n"
        response = result[:idx1-10] + breaker + code + breaker1 + result[idx2+3:]
        
        return (code, response)
    
    def serialTalk(self,code):
        pass

    # Public method to start the OpenAI run asynchronously
    async def run(self, message):
        self.addMessage(message)
        result = await self.__runManager()  # Await the result from __runManager
        return result  # Return the
