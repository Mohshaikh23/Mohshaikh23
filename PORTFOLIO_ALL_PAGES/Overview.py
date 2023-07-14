import streamlit as st
from PIL import Image
from pathlib import Path

# -- PATH SETTINGS --
def path_setting():
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    # css_file = current_dir.joinpath("styles", "main.css")
    resume_file = current_dir.joinpath("assets", "MOHSIN SHAIKH - RESUME.pdf")
    profile_pic = current_dir.joinpath("Images", "Pic1.png")
    return current_dir, resume_file, profile_pic


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

def overview_mode():
    
    current_dir, resume_file, profile_pic = path_setting()
    NAME, DESCRIPTION, EMAIL, SOCIAL_MEDIA = page_credentails()
    st.title(NAME)
    st.write(DESCRIPTION)
    download_resume()
    st.write("📫", EMAIL)