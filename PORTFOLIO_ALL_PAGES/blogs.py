import streamlit as st
from PIL import Image
import pandas as pd
from extraction import open_project

def display_blog_post():
    df = pd.read_csv('blogs_folder/blog_data.csv')
    # st.dataframe(dataframe)
    st.title("Blog Showcase")
    num_rows = len(df)

    # Divide the available space into two columns
    col1, col2 = st.columns(2)

    # Display the data in two columns
    with col1:
        for i in range(0, num_rows, 2):
            image = Image.open(df['screenshot_paths'][i])
            st.image(image, use_column_width=True)
            button_key = f"{i}_{df['blog_name'][i]}"  # Append index to make key unique
            if st.button(f"{df['blog_name'][i]}", key=button_key):
                open_project(df['blog_links'][i])
            st.markdown("---")
    with col2:
        for i in range(1, num_rows, 2):
            image = Image.open(df['screenshot_paths'][i])
            st.image(image, use_column_width=True)
            button_key = f"{i}_{df['blog_name'][i]}"  # Append index to make key unique
            if st.button(f"{df['blog_name'][i]}", key=button_key):
                open_project(df['blog_links'][i])
            st.markdown("---")

    
