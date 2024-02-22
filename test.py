from openai import OpenAI
import json

### ByteBard_XML ID
bb_id = "asst_CFsqmgnJhalDKnZvyjGKOtg7"
### PrimeBot ID
pb_id = "asst_merTUbrMxt0Fo1sc9P17G1Ax"
### Ai Alchemist ID
aa_id = "asst_8WN5ksXpnNaBeAr1IKrLq4yd"

### General test thread
thread_id = "thread_UbU1hougFO6WE4kJCmK0ylRR"

# response = openAI_assistant.callChad(
#     bb_id, thread_id, "what is the weather in lexington MA"
# )


# AI_interface = openAIAlchemy.openAIAlchemy(
#     aa_id, thread_id="thread_1GwlxP7aLrP4rQXnM2qyQmhY", debug=True
# )
# AI_interface.killAllRuns()
# # # print(AI_interface.getRuns())

# AI_interface.addMessage(
#     "write code that will drive a car and move around obstacles using an ultrasonic sensor. make sure to check with a human to ensure the car is driving correctly"
# )
# print(AI_interface.getMessage())

# simpleDict = {
#     "name": "Liam Campbell",
#     "address": {"street": "23 Edison Ave", "city": "Medford", "zipcode": "02144"},
# }

# simpleJson = json.dumps(simpleDict)
# print(simpleJson)

# complexDict = {
#     "codingGuide": {
#         "class": [
#             {
#                 "name": "motor",
#                 "description": "a class that allows access to spike prime motors",
#                 "initialization": "none",
#                 "required imports": "import motor \n from hub import port",
#                 "function": {
#                     "name": "Run motor for degrees",
#                     "syntax": "motor.run_for_degrees(port.B, 360, 75)",
#                     "parameters": {
#                         "parameter": [
#                             {
#                                 "name": "Port",
#                                 "description": "Port of spike prime to which motor is connected",
#                                 "values": "port.A,port.B,port.C,port.D,port.E,port.F",
#                             },
#                             {
#                                 "name": "Degrees",
#                                 "description": "Degrees for which the motor should turn.",
#                                 "values": "any integer",
#                             },
#                             {
#                                 "name": "Speed",
#                                 "description": "Speed at which the motor should run in degrees per second.",
#                                 "values": "any integer",
#                             },
#                         ]
#                     },
#                 },
#             },
#             {
#                 "name": "color_sensor",
#                 "description": "a class that allows access to spike prime color sensors",
#                 "initialization": "none",
#                 "required imports": "from hub import color_sensor \n from hub import port",
#                 "function": [
#                     {
#                         "name": "Color",
#                         "syntax": "color_sensor.color(port.A)",
#                         "parameters": {
#                             "parameter": {
#                                 "name": "Port",
#                                 "description": "Port of spike prime to which color sensor is connected",
#                                 "values": "port.A,port.B,port.C,port.D,port.E,port.F",
#                             }
#                         },
#                         "returns": {
#                             "name": "the color sensed by the color sensor",
#                             "values": "color.RED,color.GREEN,color.BLUE,color.MAGENTA,color.YELLOW,color.ORANGE,color.AZURE,color.BLACK,color.WHITE",
#                         },
#                     },
#                     {
#                         "name": "Reflection",
#                         "syntax": "color_sensor.reflection(port.A)",
#                         "initialization": "none",
#                         "parameters": {
#                             "parameter": {
#                                 "name": "Port",
#                                 "description": "Port of spike prime to which color sensor is connected",
#                                 "values": "port.A,port.B,port.C,port.D,port.E,port.F",
#                             }
#                         },
#                         "returns": {
#                             "name": "the intensity of light sensed by the color sensor",
#                             "values": "integer 1:100",
#                         },
#                     },
#                 ],
#             },
#             {
#                 "name": "motor_pair",
#                 "description": "a class that allows controlling two spike prime motors together",
#                 "initialization": "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
#                 "required imports": "import motor_pair \n from hub import port",
#                 "function": [
#                     {
#                         "name": "Move motor pair for degrees",
#                         "syntax": "motor_pair.move_for_degrees(motor_pair.PAIR_1, 90, 0, velocity=200)",
#                         "parameters": {
#                             "parameter": [
#                                 {
#                                     "name": "Motor Pair",
#                                     "description": "Specification of which motor pair to move",
#                                     "values": "motor_pair.PAIR_1, motor_pair.PAIR_2",
#                                 },
#                                 {
#                                     "name": "Degrees",
#                                     "description": "Degrees for which the motor pair should turn.",
#                                     "values": "any integer",
#                                 },
#                                 {
#                                     "name": "Steering",
#                                     "description": "How much the motor pair should alter motor speeds to turn",
#                                     "values": "an integer -100:100",
#                                 },
#                                 {
#                                     "name": "Velocity",
#                                     "description": "Speed at which the motors should run in degrees per second.",
#                                     "values": "any integer",
#                                 },
#                             ]
#                         },
#                     },
#                     {
#                         "name": "Move motor pair for time",
#                         "syntax": "motor_pair.move_for_time(motor_pair.PAIR_1, 1000, 0, velocity=200)",
#                         "parameters": {
#                             "parameter": [
#                                 {
#                                     "name": "Motor Pair",
#                                     "description": "Specification of which motor pair to move",
#                                     "values": "motor_pair.PAIR_1, motor_pair.PAIR_2",
#                                 },
#                                 {
#                                     "name": "Time",
#                                     "description": "Duration for which motors should turn in milliseconds (1000 = 1 second)",
#                                     "values": "any integer",
#                                 },
#                                 {
#                                     "name": "Steering",
#                                     "description": "How much the motor pair should alter motor speeds to turn",
#                                     "values": "an integer -100:100",
#                                 },
#                                 {
#                                     "name": "Velocity",
#                                     "description": "Speed at which the motors should run in degrees per second.",
#                                     "values": "any integer",
#                                 },
#                             ]
#                         },
#                     },
#                 ],
#             },
#             {
#                 "name": "distance_sensor",
#                 "description": "a class that allows access to spike prime distance sensors",
#                 "initialization": "none",
#                 "required imports": "from hub import distance_sensor \n from hub import port",
#                 "function": {
#                     "name": "Get distance",
#                     "syntax": "distance_sensor.distance(port.A)",
#                     "parameters": {
#                         "parameter": {
#                             "name": "Port",
#                             "description": "Port of spike prime to which distance sensor is connected",
#                             "values": "port.A,port.B,port.C,port.D,port.E,port.F",
#                         }
#                     },
#                     "returns": {
#                         "name": "the distance measured by the sensor in millimeters. If the distance sensor cannot read a valid distance it will return -1",
#                         "values": "integer",
#                     },
#                 },
#             },
#             {
#                 "name": "motion_sensor",
#                 "description": "a class that allows access to spike prime motion sensors",
#                 "initialization": "none",
#                 "required imports": "from hub import motion_sensor \n from hub import port",
#                 "function": [
#                     {
#                         "name": "Acceleration",
#                         "syntax": "motion_sensor.acceleration()",
#                         "parameters": "none",
#                         "returns": {
#                             "name": "a tuple containing x, y & z acceleration values as integers. The values are mili G, so 1 / 1000 G",
#                             "values": "[int, int, int]",
#                         },
#                     },
#                     {
#                         "name": "Tilt angles",
#                         "syntax": "motion_sensor.tilt_angles()",
#                         "parameters": "none",
#                         "returns": {
#                             "name": "a tuple containing yaw pitch and roll values as integers. Values are decidegrees",
#                             "values": "[int, int, int]",
#                         },
#                     },
#                     {
#                         "name": "Angular Velocity",
#                         "syntax": "motion_sensor.angular_velocity()",
#                         "parameters": "none",
#                         "returns": {
#                             "name": "a tuple containing x, y & z angular velocity values as integers. The values are decidegrees per second",
#                             "values": "[int, int, int]",
#                         },
#                     },
#                 ],
#             },
#             {
#                 "name": "sound",
#                 "description": "a class that enables control of built in SPIKE Prime speakers",
#                 "initialization": "none",
#                 "required imports": "from hub import sound \n from hub import port",
#                 "function": [
#                     {
#                         "name": "beep",
#                         "syntax": "sound.beep(freq: int = 440, duration: int = 500, volume: int = 100)",
#                         "parameters": [
#                             {
#                                 "name": "freq",
#                                 "description": "Frequency of beep",
#                                 "values": "positive integer",
#                             },
#                             {
#                                 "name": "duration",
#                                 "description": "length of beep in milliseconds",
#                                 "values": "positive integer",
#                             },
#                             {
#                                 "name": "volume",
#                                 "description": "volume of beep",
#                                 "values": "integer 1:100",
#                             },
#                         ],
#                         "returns": "none",
#                     }
#                 ],
#             },
#         ]
#     }
# }

# complexJson = json.dumps(complexDict, indent=2)

# Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(complexJson)

# file = open("queryDict.json")
# queryDict = json.loads(file.decode("utf-8"))
queryDict = json.load(open("queryDict.json", "r"))
# print(queryDict["codingGuide"]["class"][0])

for aClass in queryDict["class"]:
    if aClass["name"] == "motor":
        print(aClass)
