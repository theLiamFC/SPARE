import cv2 as cv
import base64
import time
from openai import OpenAI

client = OpenAI()

cam = cv.VideoCapture(0)
time.sleep(1)


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def imgCollection(cam, num, interval):
    images = []
    for i in range(num):
        for j in range(5):
            print(str(5 - j))
            time.sleep(1)
        print("Say cheese")
        ret, frame = cam.read()
        print("image" + str(i) + ".jpg")
        cv.imwrite("image" + str(i) + ".jpg", frame)
        base64_image = encode_image("image" + str(i) + ".jpg")
        url = f"data:image/jpeg;base64,{base64_image}"
        images.append(url)
    return images


images = imgCollection(cam, 3, 3)
content = []
content.append(
    {
        "type": "text",
        "text": "describe differences in the primary subject between images",
    }
)

for img in images:
    new_image = {
        "type": "image_url",
        "image_url": {
            "url": img,
        },
    }

    content.append(new_image)

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": content,
        }
    ],
    max_tokens=300,
)

print(response.choices[0].message.content)
