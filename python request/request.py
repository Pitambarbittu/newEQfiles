import requests

BASE_URL = "https://api.publicapis.org/entries"

req = requests.get("https://api.publicapis.org/entries")

print(req.json())

# req.content

# x = requests.get()
