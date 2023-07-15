import streamlit as st
from PIL import Image
from pathlib import Path
from extraction import load_lottiefile
from streamlit_lottie import st_lottie
import pandas as pd



# -- PATH SETTINGS --
def path_setting():
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    # css_file = current_dir.joinpath("styles", "main.css")
    resume_file = current_dir.joinpath("assets", "MOHSIN SHAIKH - RESUME.pdf")
    profile_pic = current_dir.joinpath("Images", "Pic1.png")
    css_file = current_dir.joinpath("styles", "main.css")
    return current_dir, resume_file, profile_pic, css_file


#Page Credentials
def page_credentails():
        
    NAME = "Mohsin Shaikh"
    DESCRIPTION = '''
    A Data Scientist, leveraging  data analysis, machine learning, 
    and programming skills to extract meaningful insights, 
    build predictive models, and solve complex problems.
    '''
    EMAIL = "mohsin.shaikh324@gmail.com"
    SOCIAL_MEDIA = {
        "Linkedin" : "https://www.linkedin.com/in/mohsin-shaikh-5340181b4/",
        "Github" : "https://github.com/Mohshaikh23",
        "Medium" : "https://medium.com/@mohsin.shaikh324"
    }   
    
    return NAME, DESCRIPTION, EMAIL, SOCIAL_MEDIA

#Image_loader
def load_image():
    file_path = 'Images/Pic1.png'
    image = Image.open(file_path)
    st.image(image, caption=None, use_column_width=True)

#PDF_loader
def download_resume():
    resume_file_path = 'assets/MOHSIN SHAIKH - RESUME.pdf'
    with open(resume_file_path, "rb") as file:
        resume_data = file.read()
    st.download_button("Download Resume", resume_data, file_name="resume.pdf", mime="application/pdf")

def create_button_with_link(animation, link, logo):
    button_html = f'''
        <div style="display: flex; align-items: center;">
            <div style="width: 50px; height: 50px; margin-right: 8px; overflow: hidden;">
                {st_lottie(animation, width=50, height=50)}
            </div>
            <a href="{link}" style="text-decoration: none;">{logo}</a>
        </div>
    '''
    return button_html

def logos():
    github_lottie = load_lottiefile('logos/github/animation_lk3re5a2.json')
    linkedin_lottie = load_lottiefile('logos/Linkedin/animation_lk3rpo9z.json')
    gmail_lottie = load_lottiefile('logos/GMAIL/animation_lk3ru1ji.json')
    resume_lottie = load_lottiefile('logos/Resume/animation_lk3s178d.json')
    medium_lottie = load_lottiefile('logos/Medium/animation_lk3sphvc.json')

    lottie_dict = {
        "GitHub": github_lottie,
        "LinkedIn": linkedin_lottie,
        "Gmail": gmail_lottie,
        "Resume": resume_lottie,
        "medium" : medium_lottie
    }
    
    social_dict = {
        "LinkedIn" : "https://www.linkedin.com/in/mohsin-shaikh-5340181b4/",
        "GitHub" : "https://github.com/Mohshaikh23",
        "medium" : "https://medium.com/@mohsin.shaikh324", 
        "Resume" : "https://github.com/Mohshaikh23/Mohshaikh23/blob/main/assets/MOHSIN%20SHAIKH%20-%20RESUME.pdf",
        'Gmail': f"[Send Email](mailto:{'mohsin.shaikh324@gmail.com'})"
    }
    
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]

    for logo, animation in lottie_dict.items():
        link = social_dict.get(logo)
        if link:
            column = columns.pop(0)  # Get the first column from the list of columns

            with column:
                button_html = create_button_with_link(animation, link, logo)
                st.markdown(button_html, unsafe_allow_html=True)
    
def overview_mode():
    
    current_dir, resume_file, profile_pic, css_file= path_setting()
    NAME, DESCRIPTION, EMAIL, SOCIAL_MEDIA = page_credentails()
    st.title(NAME)
    st.write(DESCRIPTION)
    download_resume()
    
    