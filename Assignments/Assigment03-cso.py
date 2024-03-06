# Assignment 3
# Student: Lais Coletta Pereira
# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# define a function that send an HTTP GET request to the URL
def getAll():
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    # open the json file, print the data from the url using the function and convert it to a json file.
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll()), file=fp)
