import os
import json
import pandas as pd
from pathlib import Path
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from streamlit import session_state
from extraction import get_github_repos , load_repositories
from classification import classify_tags
import streamlit.components.v1 as components

# -- PATH SETTINGS --

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.joinpath("styles", "main.css")
resume_file = current_dir.joinpath("assets", "MOHSIN SHAIKH - RESUME.pdf")
profile_pic = current_dir.joinpath("Images", "Pic1.png")


# -- GENERAL SETTINGS --

PAGE_TITLE = 'Digital CV | MOHSIN SHAIKH'
PAGE_ICON = ":wave:"
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

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# -- Load the CSS, PDF and Profile Pic
# with open(css_file) as f:
#     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True
with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open("E:/END TO END ML PROJECT/Mohshaikh23/Images/Pic1.png")

upper_panel = option_menu(menu_title='', 
                          options = ['OVERVIEW',
                            'EXPERIENCE',
                            'PROJECTS',
                            'BLOGS',
                            'CONTACT'],
                    #    icons=['card-text',
                    #           'person-workspace',
                    #           'briefcase',
                    #           'book',
                    #           'person-lines-fill'],
                       default_index=0, 
                       orientation='horizontal')

if upper_panel == "OVERVIEW":
    col1, col2 = st.columns(2)
    with col1:
        st.image(profile_pic, width=300)
    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name= resume_file.name,
            mime="application/octet-stream"
            )
        st.write("📫", EMAIL)

def display_experience(company, position, duration, description):
    st.subheader(f":briefcase: {company}")
    st.write(f"**{position} | {duration}**")
    st.write(description)

if upper_panel == "EXPERIENCE":
    Experience_data  = option_menu( menu_title= 'Experiences across Multiple Companies',
                                   options = ['Adappt intelligence',
                                              'Business Promoted',
                                              'Iradium Automobiles',
                                              'Sanansh Automobiles',
                                              'Kanchan Auto'],
                                    menu_icon='cast',
                                    default_index=0, 
                                    orientation='vertical')
    
    if Experience_data == 'Adappt intelligence':
        display_experience(
        "Adappt Intelligence Pvt Ltd",
        "Intern - Data Analyst",
        "October 2022 - Present",
        "- Generated Power BI reports for multiple companies, utilizing Occupancy, HVAC, and AQI data to analyze space utilization and energy consumption.\n"
        "- Processed Extract, Transform, Load (ETL) procedures from APIs to generate comprehensive Power BI reports, presenting them to clients under supervision.\n"
        "- Achieved an average improvement of 14% in space utilization, with the highest enhancement of 17%, and a remarkable 22% growth in AQI redundancy."
            )

    
    if Experience_data == 'Business Promoted':
        display_experience(
        "Business Promoted Pvt Ltd",
        "Back Office Executive",
        "June 2021 - Present",
        "- Optimized the workflow of the Repossession back-office process for a US client, leading to improved productivity and revenue generation.\n"
        "- Conducted thorough analysis of process duration, efficiency estimation, and workflow distribution, resulting in enhanced productivity and achievements."
            )

    
    if Experience_data == 'Iradium Automobiles':
        display_experience(
        "Iradium Automobile Pvt Ltd",
        "Senior Sales Executive",
        "September 2020 - February 2021",
        "- Spearheaded an 80% growth in sales from small scale to large scale, significantly expanding the customer base.\n"
        "- Implemented strategies to boost B2B sales, resulting in increased revenue and market share.\n"
        "- Successfully reduced marketing investment by 30% and improved inventory management, leading to a 10% increase in inventory turnover.\n"
        "- Achieved a 70% recovery rate on previous loans, optimizing financial performance."
            )


    
    if Experience_data == 'Sanansh Automobiles':
        display_experience(
        "Sanansh Automobiles Pvt Ltd",
        "Associate Sales Manager",
        "January 2019 - August 2020",
        "- Consistently achieved 100% sales growth with a diverse range of products including cars, bikes, and heavy vehicles.\n"
        "- Innovated new sales techniques and collaborated with marketing to reduce losses by 15% and increase insurance sales revenue by 200%.\n"
        "- Managed a team of 5 executives, fostering individual growth of approximately 30% per month."
                )


    
    if Experience_data == 'Kanchan Auto':
        display_experience(
            "Kanchan Auto Pvt Ltd",
            "Showroom Sales Manager",
            "January 2018 - January 2019",
            "- Promoted to Showroom Manager based on a 15% growth in quarter sales performance.\n"
            "- Implemented innovative marketing and strategic sales techniques, resulting in a 50% increase in accessory sales and a 30% boost in insurance sales."
                )






if upper_panel == "PROJECTS":
    st.subheader("GitHub Repositories")
    repositories = load_repositories()
    repositories["classification"] = classify_tags(repositories, 'topics')
    columns = ['name', 'html_url','description', 'classification']
    # st.dataframe(repositories[columns]) 
    repos = repositories[['name', 'html_url', 'description', 'classification']]
    classifications = repos.groupby('classification')
    
    
    classification_options = classifications.groups.keys()
    selected_classification = option_menu("Project Types", 
                                          options = list(classification_options),
                                          default_index=0, 
                                          orientation='horizontal')

    # Display the selected classification's DataFrame
    if selected_classification:
        selected_dataframe = classifications.get_group(selected_classification)
        st.subheader(f"Selected Classification: {selected_classification}")
        st.dataframe(selected_dataframe)

        

    
    

    
    
    
   

if upper_panel == "BLOGS":
    st.markdown("I write blogs here")
    
    
    
if upper_panel == "CONTACT":
    Blogs_data  = option_menu( menu_title= 'Projects across Career',
                                   options = ['Python Projects',
                                              'Machine Learning Projects',
                                              'Deep learning Projets',
                                              'Computer Vision Projects'],
                                    menu_icon='cast',
                                    default_index=0, 
                                    orientation='horizontal')




