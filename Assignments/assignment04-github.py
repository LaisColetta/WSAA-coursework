# Assignment 04
#Student: Lais Coletta Pereira
# Write a program in python that will read a file from a repository. The program should then replace all the instances of the text "Andrew" with your name
#The program should then commit those changes and push the file back to the repository. I do not need to see your keys (see lab2, to follow).

import requests
from config import config as cfg
from github import Github

filename = "assignment04.txt"
apikey = cfg["githubkey"]

name1 = "Andrew"
name2 = "Lais"

g = Github(apikey)
repo = g.get_repo("LaisColetta/aprivateone")

# Retrieve file content
file_info = repo.get_contents(filename)
response = requests.get(file_info.download_url)
file_content = response.text

# Replace text
updated_content = file_content.replace(name1, name2)

# Update file in the repository
repo.update_file(file_info.path, "Update name", updated_content, file_info.sha)

# Print updated content
print(updated_content)
