import os
import requests
import json
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
import random
import webbrowser

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

def get_image_links_from_json(json_file):
    with open(DATA_FILE_PATH, "r") as file:
        repositories = json.load(file)
    
    image_links = []
    
    for repo in repositories:
        owner = repo["owner"]
        repo_name = repo["name"]
        
        repo_contents = get_github_repos(owner, repo_name)
        
        for content in repo_contents:
            if content.get("type") == "file" and content.get("name").lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                image_links.append(content["download_url"])
    
    return image_links

def load_lottiefile(filepath:str):
    with open(filepath, 'r') as f:
        return json.load(f)

def load_lottie_url(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

   
def lottie(file_name:str):
    st_lottie(file_name,
                        speed =1,
                        reverse = False,
                        loop = True,
                        quality='low',
                        height = None,
                        width=None,
                        key=None)
    
def project_showcase():
    # Get a random animation file from the animations folder
    animation_folder = os.path.abspath("Project_lotties/")
    animation_files = os.listdir(animation_folder)
    animation_file = random.choice(animation_files)
    animation_file_path = os.path.join(animation_folder, animation_file)
    animation_files.remove(animation_file)
    animation = load_lottiefile(animation_file_path)
    
    lottie(animation)
    
def open_project(project_url):
    webbrowser.open(project_url)


def display_project(project):
    project_name = project["name"]
    project_url = project["html_url"]
    project_description = project["description"]
    
    st.subheader(project_name)
    project_showcase()
    st.write(project_description)
     
    button_key = f"view_project_{project_name}"
    if st.button("View Project", key=button_key):
        open_project(project_url)
        
    st.markdown("---")




