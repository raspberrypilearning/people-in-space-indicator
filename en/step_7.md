## An LED for each astronaut

In the next stage, you will make the number of LEDs that are on the same as the number of people in space, and get your program to run once every minute.

- You can start by removing the *testing* loop you wrote which turned all the LEDs on and off. This should leave you with a file like this:

	```python
	import requests
	from gpiozero import LED
	from time import sleep

	pins = [17, 18, 27, 22, 23, 24, 10, 25, 9, 11]
	leds = [LED(pin) for pin in pins]

	url = "http://api.open-notify.org/astros.json"
	r = requests.get(url)
	data = r.json()
	people = data['number']
	```

- You want to use an infinite loop that runs every sixty seconds. This can be achieved by using a `while True` loop and placing a `sleep(60)` inside it.

	```python
	import requests
	from gpiozero import LED
	from time import sleep

	pins = [17, 18, 27, 22, 23, 24, 10, 25, 9, 11]
	leds = [LED(pin) for pin in pins]

	url = "http://api.open-notify.org/astros.json"

	while True:
		r = requests.get(url)
		data = r.json()
		people = data['number']

		sleep(60)
	```

- Now you will get the number of LEDs lighting up to be equal to the number of people in space. You can use a `for` loop for this, just like you did in the last section. The loop should run the same number of times as the number of people in space, and illuminate a single LED for each person. Have a go at coding this, and use the hints below if you get stuck.

--- hints --- --- hint ---
1. Within the `while` loop, create a `for` loop. It should loop over `range(people)`.
2. The loop should turn on the right number of LEDs before the script sleeps for 60 seconds.
3. When the `while` loop ends, all the LEDs should turn off in preparation for the script checking whether the number of people in space has changed. Another `for` loop could accomplish this.
--- /hint --- --- hint ---
Here is some of the code - you just need to complete the areas where comments have been written.
```python
import requests
from gpiozero import LED
from time import sleep

pins = [17, 18, 27, 22, 23, 24, 10, 25, 9, 11]
leds = [LED(pin) for pin in pins]


while True:
    url = "http://api.open-notify.org/astros.json"
    r = requests.get(url)
    data = r.json()
    people = data['number']

    for i in range(people):
        ##turn on the led at position i
    sleep(60)

    for led in leds:
		##turn off the led
```
--- /hint --- --- hint ---
Here's a video showing you one way of writing the script:
<iframe width="560" height="315" src="https://www.youtube.com/embed/BiDCbI5SZrQ" frameborder="0" allowfullscreen></iframe>
--- /hint --- --- /hints ---


