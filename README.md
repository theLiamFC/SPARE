**OpenAI ChatGPT Robot Coding Interface**

This repository provides code for an iterative learning loop where a human collaborates with OpenAI's ChatGPT to code a robot in MicroPython. The essential files are main.py, openAIAlchemy.py, serial_interface.py, and queryDict.json.

**Introduction**

The aim of this project is to facilitate collaboration between humans and artificial intelligence in coding robotics applications, specifically targeting the LEGO SPIKE Prime platform. By leveraging OpenAI's ChatGPT, users can iteratively build programs alongside the AI, fostering learning opportunities for the user and accelerating robotic software projects. The program importantly flips the role of the user and AI, and enables AI to utilize the user as a resource for iterative coding development. In addition to asking the user for feedback, advice, and prompts, the AI is also enabled to query documentation, run code, and get visual feedback from a secondary OpenAI vision model.

**Usage**

To use this repository, follow these steps:
- Ensure you have Python installed on your system.
- Clone this repository to your local machine.
- Install the required dependencies, most significantly OpenAI.
- Create an OpenAI API key
- Set up you API key by following isntructions [here](https://platform.openai.com/docs/quickstart/step-2-set-up-your-api-key)
- Find the serial port of your LEGO SPIKE Prime device and update it in main.py.
- Execute main.py to start the interactive coding session with OpenAI's ChatGPT.

**File Descriptions**

openAIAlchemy.py: Contains the main class openAIAlchemy, which interfaces with the OpenAI API for communication.

main.py: Orchestrates the interaction between the user, ChatGPT, and the robot coding interface.

serial_interfacel.py: Handles all serial communication between the computer and LEGO SPIKE Prime.

queryDict.json: Contains valuable syntax and documentation for MicroPython coding on the LEGO SPIKE Prime platform.
