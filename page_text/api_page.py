import streamlit as st
from nav.page_buttons import api_page_nav_buttons
from nav.scroll_functions import scroll_page

def api_render_pages(current_page, max_page):
    #Has the page been read or not (index adjusted)
    page_is_read = st.session_state.api_page_is_read[current_page - 1]

    # Check current page and display content as appropriate
    if current_page == 1:
        api_page_one()
    elif current_page == 2:
        api_page_two()

    #Display page nav buttons
    api_page_nav_buttons(current_page, max_page)

    if st.session_state.page_nav_button_clicked:
        # Scroll tha page to top if not yet read, or bottom if already read (Only following nav. button press)
        scroll_page(page_is_read)
        # Reset page_nav_button_clicked to False
        st.session_state.page_nav_button_clicked = False

def api_page_one():
    #st.query_params.set_item("scroll", "top")
    st.header("Automated API Testing Tool")
    st.subheader("User Story")
    st.subheader("Retrieve and Display Product Information")
    st.write("""

    As a user, I want to retrieve product details via an API so that I can view and analyse product information.
    \nDescription:
    The system will provide an API endpoint: 
    \n/products 
    \nthat returns a list of products. Each product includes the following details:
    <div style="padding-left: 20px;">
        <ul>
            <li>Product ID.</li>
            <li>Title.</li>
            <li>Price.</li>
            <li>Description.</li>
            <li>Category.</li>
            <li>Image URL.</li>
            <li>Rating Information:
                <ul>
                    <li>Rate (float): The average rating.</li>
                    <li>Count (integer): The number of ratings.</li>
                </ul>
            </li>
        </ul>
    </div>
    This data can be consumed by client applications to display product information or analyse product details.
    \n<b>Acceptance Criteria</b>:
    \nSuccessful Response:
    <div style="padding-left: 20px;">
        <ul>
            <li>When a GET request is sent to /products, the API should return a 200 OK status.</li>
            <li>The response body should contain a JSON array of products.</li>
            <li>Each product should return the fields defined in the above description.</li>
        </ul>
    </div>
    Error Handling:
    <div style="padding-left: 20px;">
        <ul>
            <li>If the API is accessed with an invalid HTTP method (e.g., POST), it should return a 405 Method Not Allowed status.</li>
            <li>If the API encounters an internal server error, it should return a 500 Internal Server Error status.</li>
        </ul>
    </div>      
    Validation:
    <div style="padding-left: 20px;">
        <ul>
            <li>All fields in the response should match their expected data types.</li>
            <li>The image field must contain a valid URL.</li>
            <li>The rating.rate should be a float between 0.0 and 5.0.</li>
            <li>The rating.count should be a non-negative integer.</li>
        </ul>
    </div>            
    Performance:
    <div style="padding-left: 20px;">
        <ul>
            <li>The API should respond within 2 seconds under normal load conditions.</li>
        </ul>
    </div>         
    Security:
    <div style="padding-left: 20px;">
        <ul>
            <li>Ensure CORS (Cross-Origin Resource Sharing) policies are in place to prevent unauthorized access.</li>
            <li>API requests must only be allowed over HTTPS.</li>
        </ul>
    </div>       
    What fields returned should be:
    id (integer): A unique identifier for the product.
    title (string): The name of the product.
    price (float): The price of the product.
    description (string): A brief description of the product.
    category (string): The product's category.
    image (string): A URL to the product's image.
    rating (object): Contains:
    rate (float): The average rating.
    count (integer): The number of ratings.
    """, unsafe_allow_html=True)
    st.subheader("My Testing Approach:")
    st.write("""The first thing I would do is perform static testing on the User Story.
    This Aligns with shift-left testing strategies, 
    which emphasise the importance of involving testers early in the Software Development Life Cycle (SDLC), 
    this approach offers several key benefits:
    <div style="padding-left: 20px;">
        <ul>
            <li><b>Early Issue Detection:</b> Identifies defects early, reducing time and cost.</li>
            <li><b>Enhanced Collaboration:</b> Improves communication and understanding of requirements.</li>
            <li><b>Faster Releases:</b> Prevents delays by addressing issues upfront.</li>
            <li><b>Higher Quality:</b> Ensures continuous quality improvements.</li>
            <li><b>Cost Efficiency:</b> Minimizes expensive late-stage fixes.</li>
            <li><b>Thorough Test Coverage:</b> Enables comprehensive planning and testing.</li>
            <li><b>Reliable Builds:</b> Leads to stable, high-quality releases.</li>
        </ul>
    </div>

    """, unsafe_allow_html=True
             )

def api_page_two():
    st.header("Static Testing the User Story")
    st.write("""
            Static testing is a proactive quality assurance technique used to identify ambiguities, 
            inconsistencies, and potential defects in documentation, such as user stories, requirements, 
            and design specifications, before any code is written. 
            \nBy analysing the user story for the "Retrieve and Display Product Information" feature, 
            I will evaluate its clarity, completeness, and testability. 
            \nThis process will help uncover any gaps or ambiguities that could lead to defects 
            during implementation or dynamic testing. 
            \nThrough this analysis, I will demonstrate how static testing can enhance the quality of deliverables by
            fostering early detection and resolution of issues.
            """)
    st.header("User Story Section 1: User Story Statement and Detailed Description")

    if st.toggle("Show Analysis"):
        st.markdown(
            """
            <span style="color: rgb(255,75,75);">This statement follows the standard format: 
            "As a [user], I want to [goal], so that [benefit]." 
            <br>However, it lacks clarity on the type of user 
            (e.g., developer, end-user), which affects development and testing. 
            <br>The term "view" is vague—it's likely intended for the UI, but this should be confirmed. 
            <br>Additionally, "analyse product information" needs specifics on what this entails 
            and how the feature will be used. 
            <br>I'll compile these questions for discussion with the Product Owner and the Team. 
            <br>After reviewing, the user story will be updated to ensure it accurately reflects the requirements.</span>                  
            """
            ,unsafe_allow_html=True
        )
        st.markdown("""
            <b>As a user, I want to retrieve product details via an API so that I can view and analyse product information.</b>
            """
            ,unsafe_allow_html=True)
    else:
        st.write("""
                    As a user, I want to retrieve product details via an API so that I can view and analyse product information.
                    """)
    st.write("""
        \nDescription:
        The system will provide an API endpoint: 
        \n/products 
        \nthat returns a list of products. Each product includes the following details:
        <div style="padding-left: 20px;">
            <ul>
                <li>Product ID.</li>
                <li>Title.</li>
                <li>Price.</li>
                <li>Description.</li>
                <li>Category.</li>
                <li>Image URL.</li>
                <li>Rating Information:
                    <ul>
                        <li>Rate (float): The average rating.</li>
                        <li>Count (integer): The number of ratings.</li>
                    </ul>
                </li>
            </ul>
        </div>
        This data can be consumed by client applications to display product information or analyse product details.
        """, unsafe_allow_html=True)