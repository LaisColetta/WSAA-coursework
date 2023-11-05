# Assignment 04
#Student: Lais Coletta Pereira
# Write a program in python that will read a file from a repository. The program should then replace all the instances of the text "Andrew" with your name
#The program should then commit those changes and push the file back to the repository. I do not need to see your keys (see lab2, to follow).

import requests # Library for making HTTP requests
import json
from config import config as cfg # Import API key from a local config.py file
from github import Github

filename = "assignment04.txt"

# Personal access token with repo scope
apikey = cfg["githubkey"]

# Name to find and replace
old_name = "Andrew"
new_name = "Lais"

# Initialize the GitHub API client (reference: https://gist.github.com/mitake/4603184)
git = Github(apikey)

# Use get to access GitHub repository by owner and name (Reference: https://python.hotexamples.com/examples/github/Github/get_repo/python-github-get_repo-method-examples.html)
repository = git.get_repo("LaisColetta/aprivateone")

# Function to retrieve the content of a file from the repository
def get_file_content(filename):
    try:
        # Get the file information
        file_info = repository.get_contents(filename)

        # Retrieve and return the file content
        response = requests.get(file_info.download_url)
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to update a file in the repository
def update_file(filename, new_content, commit_message):
    try:
        # Get the file information
        file_info = repository.get_contents(filename)

        # Update the file with new content
        repository.update_file(
            file_info.path,
            commit_message,
            new_content,
            file_info.sha
        )
        print(f"File '{filename}' updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Function to replace text in a string
def replace_text(input_text, old_text, new_text):
    return input_text.replace(old_text, new_text)

# Define the text to find and replace
old_text = "Andrew"
new_text = "Lais"

# Retrieve the content of the file
file_content = get_file_content(filename)

if file_content:
    # Replace the text in the content
    updated_content = replace_text(file_content, old_text, new_text)

    # Update the file in the repository with the modified content
    update_file(filename, updated_content, "Name replacement")

    # Print the updated content
    print(updated_content)
else:
    print(f"File '{filename}' not found in the repository.")
