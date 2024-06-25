## Examining the data

The `requests` module has stored the data as a **dictionary**.

--- collapse ---
---
title: What is a dictionary?
---

Dictionaries consist of **key** and **value** pairs. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
---
fruit = {
    'a' : 'apple',
    'b' : 'banana',
    'c' : 'coconut',
    'd' : 'durian'
    }

--- /code ---

In this example, `print(fruit['a'])` would print `apple`. The **key** is `a` and the **value** is `apple`.

--- /collapse ---


The dictionary contains a value which is the number of people that are in space at the moment.

--- task ---
- Look at the data to find out the **key** you need to use. Fill in the rest of the code on line 6 to use the key to look up how many people are currently in space.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 6-7
---
import requests
url = "https://corquaid.github.io/international-space-station-APIs/JSON/people-in-space.json"
r = requests.get(url)
data = r.json()
people = 
print(people)

--- /code ---

--- /task ---

**Test:** Run your code and you should see the number of people currently in space printed on the screen.