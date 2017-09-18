## Testing your LEDs

In the previous section, you connected your LEDs to your Raspberry Pi, and hopefully tested that each one works using the **3V3** pin. Now you are going to test that you can control each LED with code.

- Make sure you have the file open on which you were working earlier. It should look something like this:

	```python
	import requests

	url = "http://api.open-notify.org/astros.json"
	r = requests.get(url)
	data = r.json()
	people = data['number']
	```

- Start by importing the code you need to control LEDs using Python:

	```python
	import requests
	from gpiozero import LED

	url = "http://api.open-notify.org/astros.json"
	r = requests.get(url)
	data = r.json()
	people = data['number']
	```

- You need to create a list containing all the GPIO pins you have used. Make sure you are adding pin numbers to the list in the sequence they are wired to the breadboard. For example, you may have wired your LEDs as shown in the following schematic:
  ![circuit](images/circuit.png)
  In that case, your list should look like this:
  
	```python
	pins = [17, 18, 27, 22, 23, 24, 10, 25, 9, 11]
	```
- Next, create an `LED` object for every pin in the list. This can be done fairly easily with a concept called **list comprehensions**. List comprehensions make it easy to create list. This line of code creates an `LED` object for each pin and adds it to a list called `led`:

	```python
	leds = [LED(pin) for pin in pins]
	```
- Save and run your code. Have a look at the `leds` list in the shell. You should see something like the following.

	```python
	>>> leds
	[<gpiozero.LED object closed>, <gpiozero.LED object closed>, <gpiozero.LED object closed>, <gpiozero.LED object closed>, <gpiozero.LED object closed>, <gpiozero.LED object closed>, <gpiozero.LED object closed>, <gpiozero.LED object closed>, <gpiozero.LED object closed>, <gpiozero.LED object closed>]
	```

- You can use this list to turn your on and off your LEDs. You just need to reference which of the ten objects in the list you want to control. This, for instance, will turn on the eighth LED:

	```python
	leds[7].on()
	```

- To test all the LEDs, you can create a loop that will turn on and off all the `LED` objects in the `leds` list. Once it's running, this should occur:

	<iframe width="560" height="315" src="https://www.youtube.com/embed/eDpoLvuIEUE" frameborder="0" allowfullscreen></iframe>

- Have a go at writing the test loop by yourself. Use the hints below if you need help.

--- hints --- --- hint ---
1. Import the `sleep` function from the time module
2. Use a `for` loop to go over each item in the `leds` list
3. Instruct each item to turn `on()`, then `sleep`, and then turn `off()`
--- /hint --- --- hint ---
Try and complete the code shown below.
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

for led in leds:
    ##turn on the led
    sleep(2)
	##turn off the led
```
--- /hint --- --- hint ---
Here's a video showing the code being written along with an explanation.
<iframe width="560" height="315" src="https://www.youtube.com/embed/HIXo7UGAJ1I" frameborder="0" allowfullscreen></iframe>
--- /hint --- --- /hints ---
