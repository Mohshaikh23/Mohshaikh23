import streamlit as st
from PIL import Image
from pathlib import Path
from extraction import load_lottiefile, open_project
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

# def create_button_with_link(animation, link, logo):
#     button_html = f"""
#     <a href="{link}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
#         <button style="background-color: 'gray'; border: None; cursor: pointer;">
#             <div style="display: flex; align-items: center;">
#                 <lottie-player src="{st_lottie(animation, width=80, height=80)}" background="transparent" speed="1" style="width: 20px; height: 20px;"></lottie-player>
#                 <span style="margin-left: -15px;">{logo}</span>
#             </div>
#         </button>
#     </a>
#     """
#     return button_html

def create_button_with_link(animation, link, logo):
    button_html = f"""
    <lottie-player src="{st_lottie(animation, width=80, height=80)}" background="transparent" speed="1" style="width: 20px; height: 20px;"></lottie-player>
    """
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

def naming_links():
    social_dict = {
        "GitHub" : "https://github.com/Mohshaikh23",
        "LinkedIn" : "https://www.linkedin.com/in/mohsin-shaikh-5340181b4/",
        'Gmail': f"[Send Email](mailto:{'mohsin.shaikh324@gmail.com'})",
        "Resume" : "https://github.com/Mohshaikh23/Mohshaikh23/blob/main/assets/MOHSIN%20SHAIKH%20-%20RESUME.pdf",
        "medium" : "https://medium.com/@mohsin.shaikh324"        
    }
    df = pd.DataFrame(data = social_dict.items(), columns=["Platform", "Link"])
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.button(df["Platform"][0], key=f"{df['Platform'][0]}_button", on_click=lambda: st.markdown(df["Link"][0], unsafe_allow_html=True))

    with col2:
        st.button(df["Platform"][1], key=f"{df['Platform'][1]}_button", on_click=lambda: st.markdown(df["Link"][1], unsafe_allow_html=True))

    with col3:
        st.button(df["Platform"][2], key=f"{df['Platform'][2]}_button", on_click=lambda: st.markdown(df["Link"][2], unsafe_allow_html=True))

    with col4:
        st.button(df["Platform"][3], key=f"{df['Platform'][3]}_button", on_click=lambda: st.markdown(df["Link"][3], unsafe_allow_html=True))

    with col5:
        st.button(df["Platform"][4], key=f"{df['Platform'][4]}_button", on_click=lambda: st.markdown(df["Link"][4], unsafe_allow_html=True))


def overview_mode():
    
    current_dir, resume_file, profile_pic, css_file= path_setting()
    NAME, DESCRIPTION, EMAIL, SOCIAL_MEDIA = page_credentails()
    st.title(':blue[ Mohsin Shaikh ]')
    st.markdown("---")
    st.write(DESCRIPTION)
    download_resume()
    
def footer_removal():
    hide_st_style = """
            <style>
            # MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

def set_custom_theme():
    # Add custom CSS styles
    st.markdown(
        """
        <style>
        /* Add your custom CSS styles here */
        /* Example:
        body {
            background-color: #b5b3ed;
            color: #262730;
        }
        */
        </style>
        """,
        unsafe_allow_html=True
    )

