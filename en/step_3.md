## The People in Space API

'API' stands for **Application Programming Interface**. This really just means a set of rules to let bits of software talk to each other. One type of API is a web API. A web API is a set of rules that lets software talk to an online server. You could use a web API to get data from a  wenserver, or get the server to do complicated processing that your computer can't do alone.

For this project, you're going to use the [International Space Station APIs](https://github.com/corquaid/international-space-station-APIs), maintained and provided for free by [Cormac Quaid](https://github.com/corquaid).

- Open up a browser window and then navigate to [https://corquaid.github.io/international-space-station-APIs/JSON/people-in-space.json](https://corquaid.github.io/international-space-station-APIs/JSON/people-in-space.json){:target="_blank"}.

- The web page shows a JSON string like this:

	```json
	{
  "number": 12,
  "iss_expedition": 71,
  "expedition_patch": "https://upload.wikimedia.org/wikipedia/commons/b/b4/ISS_Expedition_71_Patch.png",
  "expedition_url": "https://en.wikipedia.org/wiki/Expedition_71",
  "expedition_image": "https://upload.wikimedia.org/wikipedia/commons/8/81/The_official_Expedition_71_crew_portrait.jpg",
  "expedition_start_date": 1712354400,
  "expedition_end_date": 1727128800,
  ...
  }
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
