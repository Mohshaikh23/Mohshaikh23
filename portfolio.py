import os
import json
import random
import math
import pandas as pd

import streamlit as st

from streamlit_option_menu import option_menu
from streamlit import session_state

from PORTFOLIO_ALL_PAGES.Overview import overview_mode, load_image, logos
from PORTFOLIO_ALL_PAGES.Experience import experience
from PORTFOLIO_ALL_PAGES.project import project
from PORTFOLIO_ALL_PAGES.blogs import display_blog_post
from PORTFOLIO_ALL_PAGES.contact import contact


# -- GENERAL SETTINGS --
PAGE_TITLE = 'Digital CV | MOHSIN SHAIKH'
PAGE_ICON = ":wave:"

st.set_page_config(page_title= PAGE_TITLE,
                   page_icon= PAGE_ICON)

# Inject custom CSS to change background color
# st.markdown('<style>' + open('styles/main.css').read() + '</style>', unsafe_allow_html=True)

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
    logos()


if upper_panel == "EXPERIENCE":
    experience()


if upper_panel == "PROJECTS":
    project()


if upper_panel == "BLOGS":
    display_blog_post()
    
    
if upper_panel == "CONTACT":
    contact()



