from streamlit_option_menu import option_menu
import streamlit as st
from extraction import load_lottiefile, lottie

def display_experience(company, position, duration):
    st.subheader(f":briefcase: {company}")
    st.write(f"**{position} | {duration}**")

def experience():
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
            "October 2022 - Present")
        
        col1 , col2 = st.columns(2)
        with col1:
            adapt_lottie = load_lottiefile('lottie_folder/animation_lk2aiks5.json')
            lottie(adapt_lottie)
        with col2:
            st.write("- Generated Power BI reports for multiple companies, utilizing Occupancy, HVAC, and AQI data to analyze space utilization and energy consumption.\n"
            "- Processed Extract, Transform, Load (ETL) procedures from APIs to generate comprehensive Power BI reports, presenting them to clients under supervision.\n"
            "- Achieved an average improvement of 14% in space utilization, with the highest enhancement of 17%, and a remarkable 22% growth in AQI redundancy."
                )


    if Experience_data == 'Business Promoted':
        display_experience(
            "Business Promoted Pvt Ltd",
            "Project Manager",
            "June 2021 - Present")
        
        col1 , col2 = st.columns(2)
        with col1:
            business_promoted_lottie = load_lottiefile('lottie_folder/animation_lk2aph72.json')
            lottie(business_promoted_lottie)
        with col2:
            st.write("- Optimized the workflow of the Repossession back-office process for a US client, leading to improved productivity and revenue generation.\n"
            "- Conducted thorough analysis of process duration, efficiency estimation, and workflow distribution, resulting in enhanced productivity and achievements."
                        )


    if Experience_data == 'Iradium Automobiles':
        display_experience(
            "Iradium Automobile Pvt Ltd",
            "Senior Sales Executive",
            "September 2020 - February 2021")
        
        col1 , col2 = st.columns(2)
        with col1:
            iradium_lottie = load_lottiefile('lottie_folder/animation_lk2ap7sd.json') 
            lottie(iradium_lottie)
        with col2:
            st.write("- Spearheaded an 80% growth in sales from small scale to large scale, significantly expanding the customer base.\n"
            "- Implemented strategies to boost B2B sales, resulting in increased revenue and market share.\n"
            "- Successfully reduced marketing investment by 30% and improved inventory management, leading to a 10% increase in inventory turnover.\n"
            "- Achieved a 70% recovery rate on previous loans, optimizing financial performance."
                )

    if Experience_data == 'Sanansh Automobiles':
        display_experience(
            "Sanansh Automobiles Pvt Ltd",
            "Associate Sales Manager",
            "January 2019 - August 2020")
        
        col1 , col2 = st.columns(2)
        with col1:
            sanansh_lottie = load_lottiefile('lottie_folder/animation_lk2aktp5.json')
            lottie(sanansh_lottie)
        with col2:
            st.write("- Consistently achieved 100% sales growth with a diverse range of products including cars, bikes, and heavy vehicles.\n"
            "- Innovated new sales techniques and collaborated with marketing to reduce losses by 15% and increase insurance sales revenue by 200%.\n"
            "- Managed a team of 5 executives, fostering individual growth of approximately 30% per month."
                    )



    if Experience_data == 'Kanchan Auto':
        display_experience(
                "Kanchan Auto Pvt Ltd",
                "Showroom Sales Manager",
                "January 2018 - January 2019")
        
        col1 , col2 = st.columns(2)
        with col1:
            kanchan_lottie = load_lottiefile('lottie_folder/animation_lk2ajpbf.json')
            lottie(kanchan_lottie)
        with col2:
            st.write("- Promoted to Showroom Manager based on a 15% growth in quarter sales performance.\n"
                "- Implemented innovative marketing and strategic sales techniques, resulting in a 50% increase in accessory sales and a 30% boost in insurance sales."
                    )
