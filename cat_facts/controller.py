"""
controller.py
by gonzj988
Python code to make API connections
"""
import requests as re


# Global scope
def catfact(selection, num):
    facts = ""
    url = f"https://catfact.ninja/{selection}?limit=" + str(num)
    print("url:" +url)
    response = re.get(url)
    if response.ok:
        facts = get_facts(selection,response)
    else:
        facts = f"There was an error: {response.status_code}"
    return facts


def get_facts(selection,response):
    output = ""
    response_json = response.json()
    factlist = response_json["data"]
    if selection == "facts":
        for item in factlist:
            fact = item["fact"]
            output += fact + "\n"
    if selection == "breeds":
        for item in factlist:
            fact = item["breed"]
            output += fact + "\n"
    return output