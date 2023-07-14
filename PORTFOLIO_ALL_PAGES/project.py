import math

import streamlit as st
from extraction import load_repositories, display_project
from classification import classify_tags
from streamlit_option_menu import option_menu


def project():
    st.subheader("GitHub Repositories")
    repositories = load_repositories()
    repositories["classification"] = classify_tags(repositories, 'topics')
    columns = ['name', 'html_url','description', 'classification']
    # st.dataframe(repositories[columns]) 
    repos = repositories[columns]
    repos = repos.drop(repos[repos['classification'] =='Basic Projects'].index)
    classifications = repos.groupby('classification')
    
    
    classification_options = classifications.groups.keys()
    selected_classification = option_menu("Project Types", 
                                          options = list(classification_options),
                                          default_index=0, 
                                          orientation='horizontal')

   

    @st.cache_data
    def get_selected_dataframe(classification):
        return classifications.get_group(classification)

    if selected_classification:
        st.subheader(f"{selected_classification}")
        col1, col2 = st.columns(2)

        selected_dataframe = get_selected_dataframe(selected_classification)
        num_projects = len(selected_dataframe)
        max_projects_per_page = 6
        num_pages = math.ceil(num_projects / max_projects_per_page)

        page_number = st.empty()
        next_page_button = st.button("Next Page")
        
        # Retrieve the current page number
        if "page_number" not in st.session_state:
            st.session_state.page_number = 1

        # Calculate the start and end indices for the projects to be displayed on the current page
        start_index = (st.session_state.page_number - 1) * max_projects_per_page
        end_index = min(start_index + max_projects_per_page, num_projects)
        displayed_projects = selected_dataframe[start_index:end_index]

        # Calculate the number of rows per column
        num_rows = math.ceil(len(displayed_projects) / 2)

        # Iterate over the rows of the columns
        for i in range(num_rows):
            with col1:
                index1 = i * 2
                if index1 < len(displayed_projects):
                    project1 = displayed_projects.iloc[index1]
                    display_project(project1)

            with col2:
                index2 = i * 2 + 1
                if index2 < len(displayed_projects):
                    project2 = displayed_projects.iloc[index2]
                    display_project(project2)

        # Update the page number if the "Next Page" button is clicked
        if next_page_button:
            st.session_state.page_number += 1
            if st.session_state.page_number > num_pages:
                st.session_state.page_number = 1
        
        # Display the current page number and total number of pages
        page_number.markdown(f"Page: {st.session_state.page_number}/{num_pages}")