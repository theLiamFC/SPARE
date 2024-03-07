import json

test = '''{
"code": "import hub, color_sensor, motor_pair, color \n \
motor_pair.pair(motor_pair.PAIR_1, hub.port.A, hub.port.B) \n \
while True: \n \
    if color_sensor.color(hub.port.C) is color.BLUE: \n \
        motor_pair.move(motor_pair.PAIR_1, 0) \n \
    else: \n \
        motor_pair.stop(motor_pair.PAIR_1)",
"runtime": "10"
}'''

test = '''{
"code": "import"
}'''
print(test)
print("====================")
# test = test.replace("\n", "")
# print(test)
# print(json.loads(test))

temp = test.split("\n")
result = ""
for line in temp:
    if line != "\\":
        result += line + "\n"

print(result)
print(json.loads(result, strict=False))
