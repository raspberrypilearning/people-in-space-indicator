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

The `data` dictionary you just fetched contains a value which is the number of people that are in space at the moment.

--- task ---
- Look at the data to find out the **key** you need to use. Fill in the rest of the code on line 6 to use the key to look up how many people are currently in space.

--- code ---
---
language: python
line_numbers: true
line_number_start: 4
line_highlights: 6-7
---
data = r.json()
print(data)
people = 
print(people)

--- /code ---

--- collapse ---
---
title: Show me how
---

--- code ---
---
language: python
line_numbers: true
line_number_start: 6
---
people = data['number']

--- /code ---
--- /collapse ---

--- /task ---

--- task ---
+ **Test:** Run your code and you should see the number of people currently in space printed on the screen.
--- /task ---