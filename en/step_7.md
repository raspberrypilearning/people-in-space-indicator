## An LED for each astronaut

Display the number of people in space using your LEDs. The number will update once per minute.

--- task ---

+ Remove the code you used to turn on LEDs in the previous step.

--- /task ---

--- task ---
- Modify your code to add an infinite loop that waits sixty seconds before running again. Indent your previous code to fetch the data from the API so that it is inside the loop. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 3, 9, 14
---
import requests
from gpiozero import LEDBarGraph
from time import sleep

leds = LEDBarGraph(21, 20, 16, 12, 8, 25, 24, 23, 18, 14)

url = "https://corquaid.github.io/international-space-station-APIs/JSON/people-in-space.json"

while True:
	r = requests.get(url)
	data = r.json()
	people = data['number']
	print(people)
	sleep(60)

--- /code ---
--- /task ---



--- task ---
- Light a number of LEDs equal to the number of people in space. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 9
line_highlights: 14-15
---
while True:
	r = requests.get(url)
	data = r.json()
	people = data['number']
	print(people)
	leds.off()
	leds.value = people/10
	sleep(60)

--- /code ---

--- /task ---
