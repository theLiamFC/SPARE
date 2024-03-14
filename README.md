**OpenAI ChatGPT Robot Coding Interface**

This repository is a work in progress authored by Jesse Gilbert and Liam Campbell for the Center for Engineering & Education Outreach ([CEEO](https://ceeo.tufts.edu/)) at Tufts University.

**Introduction**

The aim of this project is to facilitate collaboration between humans and artificial intelligence in coding robotics applications, specifically targeting the LEGO SPIKE Prime platform. By leveraging OpenAI's ChatGPT, users can iteratively build programs alongside the AI, fostering learning opportunities for the user and accelerating robotic software projects. The program importantly flips the role of the user and AI, and enables AI to utilize the user as a resource for iterative coding development. In addition to asking the user for feedback, advice, and prompts, the AI is also enabled to query documentation, run code, and get visual feedback from a secondary OpenAI vision model.

**Usage**

To use this repository, follow these steps:
- Ensure you have Python installed on your system.
- Clone this repository to your local machine.
- Install all required dependencies, most significantly OpenAI.
- Create an OpenAI API key
- Set up your API key by following isntructions [here](https://platform.openai.com/docs/quickstart/step-2-set-up-your-api-key)
- Find the serial port of your LEGO SPIKE Prime device and update it in main.py.
- Execute main.py to start the interactive coding session with OpenAI's ChatGPT.

**File Descriptions**

openAIAlchemy.py: Contains the main class openAIAlchemy, which interfaces with the OpenAI API for communication.

main.py: Orchestrates the interaction between the user, ChatGPT, and the robot coding interface.

serial_interfacel.py: Handles all serial communication between the computer and LEGO SPIKE Prime.

queryDict.json: Contains valuable syntax and documentation for MicroPython coding on the LEGO SPIKE Prime platform. It is ultimately the hope that this json file would be replaced by documentation built into the microcontroller itself. For now we are using this isolated json documentation file to mimic the idea that the AI model has no pre-established knowledge of the robotic platform it is programming.
