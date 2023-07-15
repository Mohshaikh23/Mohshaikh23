from extraction import get_github_repos

def refreshing_repos():
    DATA_FILE_PATH = "Repos/repositories.json"
    get_github_repos(username='Mohshaikh23')

import streamlit as st

def refresh():
    # Define your authentication credentials
    valid_username = "mohsin.shaikh324@gmail.com"
    valid_password = "Mohsin@007"

    # Create a session state to store the authentication status
    session_state = st.session_state

    # Check if the user is authenticated
    if "authenticated" not in session_state:
        # If not authenticated, show the login form
        st.markdown("---")
        st.markdown("For Admin use only")
        st.write("Please log in to access the dataset refresh page.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Log in"):
            if username == valid_username and password == valid_password:
                session_state["authenticated"] = True
                st.success("Successfully logged in!")
                refreshing_repos()
            else:
                st.error("Invalid username or password.")
    else:
        # If authenticated, show the dataset refresh page
        st.title("Dataset Refresh Page")
        st.write("You can refresh the dataset here.")

        # Perform the dataset refresh logic
        if st.button("Refresh Dataset"):
            # Add your code here to refresh the dataset
            st.success("Dataset refreshed successfully!")
