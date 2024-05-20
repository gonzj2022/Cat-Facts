"""
controller.py
by gonzj988
Python code to make API connections
"""
import requests as re

# Global scope
def catfact(user_sel1, user_sel2):
    if user_sel1 == 0:
        url = "https://catfact.ninja/facts?max_lenght=200&limit=" + str(user_sel2)
        response = re.get(url)
        if response.ok:
            print(response.text)
        else:
            print(f"There was an error: {response.status_code}")
    if user_sel1 == 1:
        url = "https://catfact.ninja/breeds?limit=" + str(user_sel2)
        response = re.get(url)
        if response.ok:
            print(response.text)
        else:
            print(f"There was an error: {response.status_code}")