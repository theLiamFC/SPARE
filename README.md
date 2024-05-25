# Research in Autonomous AI Driven Robotics

**See our project write-up and demo videos [here](https://jessewgilbert.com/294c737d316f4b9d8a770d69897d39aa)**

This repository is authored by [Jesse Gilbert](https://jessewgilbert.com/) and [Liam Campbell](https://liamfcampbell.com/) for the Center for Engineering & Education Outreach ([CEEO](https://ceeo.tufts.edu/)) at Tufts University.

### Introduction

This project aims to explore the role that AI can play in coding robotics in two parts…

#### **Program for AI Robotics Engineering (PARE) - Repo [here](https://github.com/theLiamFC/PARE):**

Focuses on the core capabilities of AI-programmed robotics, such as **autonomous decision making**, **direct hardware control,** **iterative coding**, and **independent verification** of success.

#### **Scaffolded Program for AI Robotics Engineering (SPARE) - This repo:**

Builds on the foundation of PARE but introduces a **network** of manager and worker AI Assistants. This **hierarchical system** experiments with the execution of **more complex tasks**, that address multiple microcontrollers, by delegating them to sub-workers and **abstracting** them from the user.

### Usage

To use this repository, follow these steps:

- Ensure you have Python installed on your system.
- Clone this repository to your local machine.
- Install all required dependencies:
    - `pip install openai` (for calling the OpenAI API)
    - `pip install opencv-python` (for capturing images for the get_visual_feedback function)
    - `pip install pillow` (for opening images for the get_visual_feedback function)
    - `pip install serial` (for communicating with the robot of USB)
- Create an OpenAI API key [here](https://platform.openai.com/api-keys).
- Set up your API key by following the instructions [here](https://platform.openai.com/docs/quickstart/step-2-set-up-your-api-key).
- Plug in your LEGO SPIKE Prime to your computer and turn it on.
- Find the serial port of your LEGO SPIKE Prime device and update it in `main.py`.
- Run `main.py` to start the interactive AI powered coding session.

### File Descriptions

`main.py`: Orchestrates the interaction between the user and the top-level AI manager.

`ai_alchemy.py`: Contains the class AIAlchemy, which provides the framework for OpenAI's AI model to interface with the user, the robot, documentation, sub-worker AI assistants, manager AI assistants, etc.

`serial_interface.py`: Handles all serial communication between the computer and microcontrollers.

`search_documentation.py`: Provides functions that let the AiAlchemy class access documentation for various microcontrollers

`doc_files/`: Contains doc files with necessary syntax and documentation for MicroPython coding on various microcontrollers (LEGO SPIKE Prime, OpenMV camera, and Raspberry Pi Pico). Ultimately we hope this will be replaced by documentation built into the microcontroller. For now, we are using this isolated JSON documentation to mimic the idea that the AI model has no pre-established knowledge of the robotic platform it is programming.

`log_printing_gui.py`: Displays the workings of each subworker
