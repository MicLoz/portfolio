import streamlit as st
from colour_picker import colour_picker_section, return_custom_styling
from api_validation import display_api_streamlit_elements
from page_text.home_page import home_page_text
from page_text.api_page import api_render_pages

# Initialize session state variables for api project page navigation
if "api_current_project_page" not in st.session_state:
    st.session_state.api_current_project_page = 1  # Default to the first page of the project
if "api_page_is_read" not in st.session_state:
    st.session_state.api_page_is_read = [False,False,False] # Stores if pages have been read by the user or not.
if "page_nav_button_clicked" not in st.session_state:
    st.session_state.page_nav_button_clicked = False # Denotes if Next or Previous buttons were clicked, prior to page reload

#Titles and Sidebar config.
st.title("Michael Lozynsky : Portfolio")
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select a Project", ["Home",
                                                   "Automated API Testing Tool",
                                                   "Automated Testing Framework with Python",
                                                   "ELT Pipeline for Data Processing (Python + SQL + DBT)",
                                                   "API Testing & Integration (Postman, Swagger, Python)",
                                                   "Data Analysis & Reporting Dashboard (Python, Pandas, SQL)",
                                                   "Data Quality Dashboard (Python + Flask/Django)",
                                                   "Automated Deployment & CI/CD Pipeline (GitHub Actions, Docker, Python)"
                                                   ])
st.sidebar.title("Customisation")
with st.sidebar.expander("Customise Theme Colours"):
    theme_colours = colour_picker_section()

custom_style = return_custom_styling(theme_colours)
st.markdown(custom_style, unsafe_allow_html=True)

if option == "Home":
    home_page_text()

elif option == "Automated API Testing Tool":
    #Set maximum no. of pages and retrieve current page for this Project
    max_page = 3
    current_page = st.session_state.api_current_project_page

    # Check current page and display content as appropriate
    api_render_pages(current_page, max_page)

    #display_api_streamlit_elements() # Commented out for now, this shows the API testing tool.

elif option == "Automated Testing Framework with Python (Playwright)":
    st.header("Automated Testing Framework with Python and Playwright")
    st.write("Description of the project.")

elif option == "ELT Pipeline for Data Processing (Python + SQL + DBT)":
    st.header("ELT Pipeline for Data Processing with Python, SQL + DBT)")
    st.write("Details about the ELT Pipeline you built.")

elif option == "API Testing & Integration (Postman, Swagger, Python)":
    st.header("API Testing & Integration with Postman, Swagger and Python")
    st.write("Description.")

elif option == "Data Analysis & Reporting Dashboard (Python, Pandas, SQL)":
    st.header("Data Analysis & Reporting Dashboard with Python, Pandas and SQL")
    st.write("Description.")

elif option == "Data Quality Dashboard (Python + Flask/Django)":
    st.header("Data Quality Dashboard with Python and Flask/Django")
    st.write("""Description: Create a web app with Flask or Django that visualizes data quality metrics for a database, showing which records have issues or need cleaning.
    Skills Highlighted: Python, Flask/Django, data quality, web development.
    Why It Fits: This project could showcase both your Python skills and your ability to work with databases, while also demonstrating a hands-on approach to ensuring data quality..""")

elif option == "Automated Deployment & CI/CD Pipeline (GitHub Actions, Docker, Python)":
    st.header("Automated Deployment & CI/CD Pipeline (GitHub Actions, Docker, Python)")
    st.write(   """
    
                """
             )


