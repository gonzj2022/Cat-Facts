"""
controller.py
by gonzj988
Python code to make API connections
"""
import requests as re


# Global scope
def catfact(selection, num):
    facts = ""
    url = f"https://catfact.ninja/{selection}?max_lenght=200&limit=" + str(num)
    response = re.get(url)
    if response.ok:
        facts = get_facts(response)
    else:
        facts = f"There was an error: {response.status_code}"
    return facts


def get_facts(response):
    output = ""
    response_json = response.json()
    factlist = response_json["data"]
    for item in factlist:
        fact = item["fact"]
        output += fact + "/n"
    return output