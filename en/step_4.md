## Examining the data

Now that you have stored the web page data, you can have a look at it in more detail. The `requests` module has stored the data as a simple Python dictionary. What you need to know is the number of people that are in space at the moment.

Have a look at the section below if you need to learn how to use dictionaries in Python.

[[[generic-python-basic-dictionaries]]]

- Use the `data` dictionary you have to find the number of people in space and store it as a variable called `people`.

--- hints --- --- hint ---
Don't forget that the `key` in this dictionary is a string. So you'll need to look up its `'number'` using quotes `'`.
--- /hint --- --- hint ---
Here's some incomplete code to help you out:

```python
import requests
url = "http://api.open-notify.org/astros.json"
r = requests.get(url)
data = r.json()
people = data[SOMETHING GOES HERE]
```
--- /hint --- --- hint ---
Have a look at the video below to see how to inspect the data in the dictionary.
<iframe width="560" height="315" src="https://www.youtube.com/embed/gMeKNygN9A4" frameborder="0" allowfullscreen></iframe>
--- /hint --- --- /hints ---
