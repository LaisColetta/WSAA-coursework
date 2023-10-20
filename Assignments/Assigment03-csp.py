import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

# Define a function to retrieve data from the web service
def getAll():
    # Send an HTTP GET request to the specified URL
    response = requests.get(url)
    # Return the JSON response from the web service
    return response.json()

# Main code block
if __name__ == "__main__":
    # Open a file named "cso.json" in write text mode
    with open("cso.json", "wt") as fp:
        # Retrieve data from the web service using the 'getAll' function,
        # convert it to a JSON string, and write it to the "cso.json" file.
        print(json.dumps(getAll()), file=fp)
