import streamlit as st

def home_page_text():
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