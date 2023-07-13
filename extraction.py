import os
import requests
import json
import pandas as pd

DATA_FILE_PATH = "Repos/repositories.json"

def get_github_repos(username):
    # Check if the data file exists
    if os.path.exists(DATA_FILE_PATH):
        # Load repositories from the data file
        with open(DATA_FILE_PATH, "r") as file:
            repositories = json.load(file)
    else:
        # Fetch repositories from the GitHub API
        response = requests.get(f"https://api.github.com/users/{username}/repos")
        if response.status_code == 200:
            repositories = response.json()
            # Save repositories to the data file
            with open(DATA_FILE_PATH, "w") as file:
                json.dump(repositories, file)
        else:
            repositories = []

    return repositories

# get_github_repos(username='Mohshaikh23')

def load_repositories():
    repositories = pd.read_json(DATA_FILE_PATH)
    df= pd.DataFrame(repositories)
    return df