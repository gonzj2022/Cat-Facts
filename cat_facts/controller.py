"""
controller.py
by gonzj988
Python code to make API connections
"""
import requests as re
url = "https://catfact.ninja/fact"

response = re.get(url)

if response.ok:
    print(response.text)
else:
    print(f"There was an error: {response.status_code}")