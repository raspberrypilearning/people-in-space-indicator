import requests
url = "https://corquaid.github.io/international-space-station-APIs/JSON/people-in-space.json"
r = requests.get(url)

print(r)

data = r.json()

print(data["number"])