## Control the LEDs with code

Now that your LEDs are set up, you can control each LED with code.

--- task ---
+ Re-open the Python file you started earlier. 

+ Import `gpiozero` which allows you to control LEDs using Python:

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 2
---
import requests
from gpiozero import LEDBarGraph
url = "https://corquaid.github.io/international-space-station-APIs/JSON/people-in-space.json"
r = requests.get(url)
data = r.json()
print(data)
people = data['number']
print(people)

--- /code ---

--- /task ---

You will use the `LEDBarGraph` class to draw a bar graph using the LEDs. 

--- collapse ---
---
title: How does LEDBarGraph work?
---
If the bar graph's value is set to 1, all the LEDs are lit. If it's set to 0, none are lit. When set to 1/2 or 0.5, the first half of the LEDs are lit. Any other fraction or value between 0 and 1 can be used.

--- /collapse ---

--- task---
+ Create an LED Bar Graph containing all the GPIO pins you are using. The numbers in the brackets are the pin numbers, so write the numbers in the same order you wired the LEDS to the breadboard. For example:

--- code ---
---
language: python
line_numbers: true
line_number_start: 7
line_highlights: 9
---
people = data['number']
print(people)
leds = LEDBarGraph(17, 18, 27, 22, 23, 24, 10, 25, 9, 11)

--- /code ---
	
--- /task ---

--- task ---
+ Test that your LEDs work using the `on` method to turn them all on. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 7
line_highlights: 10
---
people = data['number']
print(people)
leds = LEDBarGraph(17, 18, 27, 22, 23, 24, 10, 25, 9, 11)
leds.on()

--- /code ---
--- /task ---

--- task ---
+ Delete the `leds.on()` code.

+ To light up half of the LEDs, set the bar graph value to the fraction of LEDs you want lit:

--- code ---
---
language: python
line_numbers: true
line_number_start: 7
line_highlights: 10
---
people = data['number']
print(people)
leds = LEDBarGraph(17, 18, 27, 22, 23, 24, 10, 25, 9, 11)
leds.value = 5/10

--- /code ---

+ Try other fractions to light up different numbers of LEDs.

--- /task ---

