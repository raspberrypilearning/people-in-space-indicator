## The People in Space API

'API' stands for **Application Programming Interface**. This really just means a set of rules to let bits of software talk to each other. One type of API is a web API. A web API is a set of rules that lets software talk to an online server. You could use a web API to get data from a  wenserver, or get the server to do complicated processing that your computer can't do alone.

For this project, you're going to use the [People in Space API](http://open-notify.org/Open-Notify-API/People-In-Space/), maintained and provided for free by [Nathan Bergey](http://open-notify.org/about).

- Open up a browser window and then navigate to [http://api.open-notify.org/astros.json](http://api.open-notify.org/astros.json){:target="_blank"}.

- The web page shows a JSON string like this:

	```json
	{"people": [{"name": "Anton Shkaplerov", "craft": "ISS"}, {"name": "Scott Tingle", "craft": "ISS"}, {"name": "Norishige Kanai", "craft": "ISS"}, {"name": "Oleg Artemyev", "craft": "ISS"}, {"name": "Andrew Feustel", "craft": "ISS"}, {"name": "Richard Arnold", "craft": "ISS"}], "number": 6, "message": "success"}
	```

- When you see data being presented like this, it is usually **JSON** data. This stands for **JavaScript Object Notation**. JSON is great for sending data between different computer systems and software, because it really doesn't matter which language you are programming in.

- Your first task is to use the `requests` module in Python to fetch the data you can see in your web browser.

[[[generic-python-requests]]]

Now see if you can fetch the data from the People In Space API using the `requests` module.

--- hints --- --- hint ---
Here's the steps you'll need to follow:
- Import the `requests` module
- Store the People In Space API URL as a variable
- Fetch the page's data using `requests.get()`
- Store the **JSON** content from the page as data
--- /hint --- --- hint ---
Here's a partially completed script that you can use as a start:
```python
import requests
url =
r = requests.get(  )
data =
```
--- /hint --- --- hint ---
Here's a video showing you what to do:
<iframe width="560" height="315" src="https://www.youtube.com/embed/3gNCeWMdU1Y" frameborder="0" allowfullscreen></iframe>
--- /hint --- --- /hints ---
