from gpiozero import LED
import requests
from time import sleep

pins = [2, 3, 4, 14, 15, 17, 18, 27, 22, 23]
leds = [LED(p) for p in pins]

url = "http://api.open-notify.org/astros.json"

while True:
    r = requests.get(url)
    j = r.json()
    n = j['number']
    for i, led in enumerate(leds):
        if n > i:
            led.on()
        else:
            led.off()
    sleep(60)  # update every minute
