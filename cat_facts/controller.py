"""
controller.py
by gonzj988
Python code to make API connections
"""
import requests as re


# Global scope
def catfact(selection):
    if selection == "facts":
        facts = ""
        url = f"https://catfact.ninja/fact"
        response = re.get(url)
        if response.ok:
            facts = get_facts(selection,response)
        else:
            facts = f"There was an error: {response.status_code}"
    if selection == "breeds":
        facts = ""
        #maximum number of breeds is 98
        url = f"https://catfact.ninja/breeds?limit=98"
        response = re.get(url)
        if response.ok:
            facts = get_facts(selection,response)
        else:
            facts = f"There was an error: {response.status_code}"
    return facts

def get_facts(selection,response):
    output = ""
    response_json = response.json()
    if selection == "facts":
        output = response_json["fact"]
    if selection == "breeds":
        factlist = response_json["data"]
        for item in factlist:
            fact = item["breed"]
            output += fact + "\n"
    return output