import streamlit as st
from colour_picker import colour_picker_section, return_custom_styling

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
    st.header("About Me")
    st.write("""
                With over seven years of experience in the software industry, 
                I’ve built a strong foundation in QA, while developing a deep passion for application development 
                and working with data, particularly through Python.
                \nI’m proficient in Python, SQL, and C#, using these skills for automated test scripting 
                (Selenium, Playwright) and validating complex data sets. 
                \nI’ve also worked on ELT processes 
                and data modeling with DBT and Snowflake.
                My testing experience spans diverse software applications, including:
                <div style="padding-left: 20px;">
                    <ul>
                        <li>User portals.</li>
                        <li>Financial reports.</li>
                        <li>Job field management software.</li>
                        <li>Online retail platforms.</li>
                        <li>APIs.</li>
                        <li>CRMs.</li>
                    </ul>
                </div>
                Collaborating with international teams, I played a key role in improving team practices 
                and promoting a culture of quality across development stages.
                \nAs a Scrum Master, I helped manage team activities, ensuring effective communication and 
                collaboration. 
                \nI also played a key role in training developers on best testing practices, 
                fostering a culture where quality was everyone's responsibility.
                \nTo further promote knowledge sharing, I ran internal workshops to upskill developers in writing 
                high-quality, performant SQL.
                \nDriven by my desire to move beyond traditional QA, I’m eager to transition into roles that blend 
                quality assurance with development and data engineering.
                \nWith my Python expertise and passion 
                for automation, I’m excited to continue growing as a Python-focused professional, 
                committed to creating efficient, high-quality software solutions.
                \nI invite you to explore the projects in this portfolio, 
                which showcase my skills and the value I can bring to your company.
                \nThe Projects are available under the left hand "Navigation" pane within the "Select a  Project" dropdown.
             """, unsafe_allow_html=True
             )

elif option == "Automated API Testing Tool":
    st.header("Automated API Testing Tool")
    st.subheader("My Brief:")
    st.write("""Build an interactive API testing tool where users can input API endpoints 
             and see the responses in real-time. 
             This can be done using Postman or Python requests and can display the status, 
             response time, and data returned by the API."""
             )

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


