from gpiozero import LED
import requests
from time import sleep

pins = [9, 22, 8, 18, 7, 17, 25, 23, 24]  # choose your own pin numbers - these are the SnowPi pins
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