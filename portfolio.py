import os
import json
import random
import math
import pandas as pd

import streamlit as st

from streamlit_option_menu import option_menu
from streamlit import session_state
from extraction import get_github_repos , load_repositories, load_lottie_url, load_lottiefile,lottie, project_showcase,display_project
from classification import classify_tags
import streamlit.components.v1 as components

from PORTFOLIO_ALL_PAGES.Overview import overview_mode, load_image
from PORTFOLIO_ALL_PAGES.Experience import experience
from PORTFOLIO_ALL_PAGES.project import project


# -- GENERAL SETTINGS --
PAGE_TITLE = 'Digital CV | MOHSIN SHAIKH'
PAGE_ICON = ":wave:"
st.set_page_config(page_title= PAGE_TITLE, 
                   page_icon= PAGE_ICON)


upper_panel = option_menu(menu_title='', 
                          options = ['OVERVIEW','EXPERIENCE','PROJECTS',
                                     'BLOGS','CONTACT'],
                          default_index=0,
                          orientation='horizontal')

if upper_panel == "OVERVIEW":
    col1, col2 = st.columns(2)
    with col1:
        load_image()
    with col2:
        overview_mode()
        
if upper_panel == "EXPERIENCE":
    experience()

if upper_panel == "PROJECTS":
    project()

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




