import requests
import json
from config import config as cfg

filename = "repos-private.json"
url = 'https://github.com/LaisColetta/PrivateforLab4'
apikey = "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"

response = requests.get(url, auth=('token', apikey))

repoJSON = response.json()

if response.status_code == 200:
    repoJSON = response.json()
    with open(filename, 'w') as fp:
        json.dump(repoJSON, fp, indent=4)
    print(f'Repository information written to {filename}')
else:
    print(f'Failed to retrieve repository information. Status code: {response.status_code}')