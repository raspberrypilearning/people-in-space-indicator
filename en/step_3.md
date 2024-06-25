## The People in Space API

'API' stands for **Application Programming Interface**. A web API is a set of rules that lets software talk to an online server. 

For this project, you're going to use the [International Space Station APIs](https://github.com/corquaid/international-space-station-APIs), maintained and provided for free by [Cormac Quaid](https://github.com/corquaid).

--- task ---
+ Open this link in a web browser [https://corquaid.github.io/international-space-station-APIs/JSON/people-in-space.json](https://corquaid.github.io/international-space-station-APIs/JSON/people-in-space.json){:target="_blank"}

--- /task ---

The web page shows some data in a format called JSON:

--- code ---
---
language: json
line_numbers: false
---
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
--- /code ---

--- task ---
+ Open a new **Python file**

+ Use the `requests` module to load the data into Python.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
---
import requests
url = "https://corquaid.github.io/international-space-station-APIs/JSON/people-in-space.json"
r = requests.get(url)
data = r.json()
print(data)

--- /code ---

--- /task ---

--- task ---
+ **Test:** Run your program and you should see the JSON data printed on the screen.

--- /task ---