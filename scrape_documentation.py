import requests
import json
from bs4 import BeautifulSoup
import re

htmlArray = [
    "https://docs.openmv.io/library/pyb.html",
    "https://docs.openmv.io/library/stm.html",
    "https://docs.openmv.io/library/omv.sensor.html",
    "https://docs.openmv.io/library/omv.image.html",
    "https://docs.openmv.io/library/omv.tf.html",
    "https://docs.openmv.io/library/omv.gif.html",
    "https://docs.openmv.io/library/omv.mjpeg.html",
    "https://docs.openmv.io/library/omv.audio.html",
    "https://docs.openmv.io/library/omv.micro_speech.html",
    "https://docs.openmv.io/library/omv.display.html",
    "https://docs.openmv.io/library/omv.fir.html",
    "https://docs.openmv.io/library/omv.tv.html",
    "https://docs.openmv.io/library/omv.cpufreq.html",
    "https://docs.openmv.io/library/omv.buzzer.html",
    "https://docs.openmv.io/library/omv.imu.html",
    "https://docs.openmv.io/library/omv.rpc.html",
    "https://docs.openmv.io/library/omv.rtsp.html",
    "https://docs.openmv.io/library/omv.omv.html",
    "https://docs.openmv.io/library/math.html",
    "https://docs.openmv.io/library/time.html",
    "https://docs.openmv.io/library/random.html",
]

documentation = {}

for num,link in enumerate(htmlArray):
    # chunks = link.split(".","/")
    chunks = re.split("[/.]", link)
    title = chunks[len(chunks)-2]

    thisDoc = {}

    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")

    for line in soup.get_text().split("\n\n"+title+"."):
        findFunc = line.split("(")
        if len(findFunc[0]) < 20:
            thisDoc[findFunc[0]] = line

    documentation[title] = thisDoc

json_data = json.dumps(documentation)
with open("openMV_Documentaton.json", "w") as outfile:
    outfile.write(json_data)
