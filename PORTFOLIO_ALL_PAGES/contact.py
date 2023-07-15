import streamlit as st  

# st.header(":mailbox: Get In Touch With Me!")

def form():
    
    contact_form = """
    <form action="https://formsubmit.co/mohsin.shaikh324@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)
    
def css_connection():
    css_file = "styles/form.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
def contact():
    form()
    css_connection()
    
    