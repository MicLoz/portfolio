import streamlit as st

def api_render_pages(page_to_render):
    if page_to_render == 1:
        api_page_one()

def api_page_one():
    #st.query_params.set_item("scroll", "top")
    st.header("Manual Testing - Page 01")
    st.subheader("Subheader1")
    st.subheader("Subheader2")
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

    if st.toggle("Show Analysis", key="us_statement_toggle"):
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
    if st.toggle("Show Analysis", key="us_body_toggle"):
        st.markdown(
            """
            <span style="color: rgb(255,75,75);">
                The first three lines of this section clearly give us the endpoint and its function.  
                <br>But once we reach the bullet-pointed list of elements to be returned, only two of the elements specify 
                the expected data types and provide more detail about the actual data these elements represent:  
                <br>
                <br>- Rate (float): The average rating. 
                <br>- Count (integer): The number of ratings.                
                <br>
                <br>To improve the accuracy and clarity of this user story, we need to know the expected data types for each element, 
                along with a brief description of their purpose.  
                <br>
                <br>In order to validate the values the ratings elements return, I would need access to the database storing these ratings, which I assume is in a related table such as `product_ratings`.  
                We’ll add these points to our list of questions for the Product Owner and wider team.                
                Other considerations include:
                <ul>
                    <li>What is the expected format for the Product ID? Is it numeric, alphanumeric, or something else?</li>
                    <li>Should the Title have a character limit?</li>
                    <li>Are Description and Category mandatory? What happens if they are empty or null?</li>
                    <li>How should the API handle invalid Image URLs? Should it omit them from the response or include a placeholder?</li>
                    <li>If the image URL is valid, how do we validate that the image returned is the correct one for the product?</li>
                    <li>Should <code>rating.rate</code> default to <code>0.0</code> or <code>null</code> if no ratings exist? What about <code>rating.count</code>?</li>
                    <li>Is there a specific format for error messages in the response body for 405 and 500 errors? Should they include details such as timestamps or request IDs?</li>
                    <li>What should the API return if the product list is empty? Should it include an empty array with a 200 OK status or something else?</li>
                </ul>                
                I will discuss these points with the Product Owner and team to ensure accurate requirements and validation.
                <br>It's worth noting that this part of the user story states:
                <br>"This data can be consumed by client applications to display product information or analyse product details."
                <br>So our earlier assumption that this API will be used to display product information to an end user is correct,
                we need not query this with the PO and team. 
                <br>The question around exactly what "analyse product details" entails
                still stands, for example if the user needs the data to be returned in a certain format as part of their analysis
                this information will help direct the development and testing approach we use for this piece of work.
            </span>          
            """, unsafe_allow_html=True
        )
        st.markdown("""<b>
            <br>Description:
            The system will provide an API endpoint: 
            <br>/products 
            <br>that returns a list of products. Each product includes the following details:
            <div style="padding-left: 20px;">
                <ul>
                    <b>
                        <li>Product ID.</li>
                        <li>Title.</li>
                        <li>Price.</li>
                        <li>Description.</li>
                        <li>Category.</li>
                        <li>Image URL.</li>
                        <li>Rating Information:
                            <ul>
                                <b>
                                    <li>Rate (float): The average rating.</li>
                                    <li>Count (integer): The number of ratings.</li>
                                </b>
                            </ul>
                        </li>
                    </b>
                </ul>
            </div>
            This data can be consumed by client applications to display product information or analyse product details.
            </b>""", unsafe_allow_html=True)
    else:
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

def api_page_three():
    st.header("Static Testing the User Story")
    st.write("<b>Acceptance Criteria:</b>", unsafe_allow_html=True)
    if st.toggle("Show Analysis", key="api_suc_resp"):
        st.markdown("""
            <span style="color: rgb(255,75,75);">
                This acceptance criteria gives us a good understanding of how the feature should function.
                But the queries raised in earlier analysis still stand.
            </span>
            """, unsafe_allow_html=True)
        st.write("""
            \n<b>Successful Response:</b>
            <div style="padding-left: 20px;">
                <ul>
                    <b>
                        <li>When a GET request is sent to /products, the API should return a 200 OK status.</li>
                        <li>The response body should contain a JSON array of products.</li>
                        <li>Each product should return the fields defined in the above description.</li>
                    </b>
                </ul>
            </div>
            """
            ,unsafe_allow_html=True)
    else:
        st.write("""
            \nSuccessful Response:
            <div style="padding-left: 20px;">
                <ul>
                    <li>When a GET request is sent to /products, the API should return a 200 OK status.</li>
                    <li>The response body should contain a JSON array of products.</li>
                    <li>Each product should return the fields defined in the above description.</li>
                </ul>
            </div>
            """
            ,unsafe_allow_html=True)
    if st.toggle("Show Analysis", key="api_err_hand"):
        st.markdown("""
            <span style="color: rgb(255,75,75);">
                This gives us more detail on the types of error expected for 405 and 500 error codes.
                <br>It is still worth asking: "Should the error responses include details such as timestamps or request IDs?"
                <br>As this may make the delivered solution more user friendly and improve it's overall quality.
                <br>
            </span>
            """, unsafe_allow_html=True)
        st.write("""
        <b>Error Handling:</b>
        <div style="padding-left: 20px;">
            <ul>
                 <b>
                    <li>If the API is accessed with an invalid HTTP method (e.g., POST), it should return a 405 Method Not Allowed status.</li>
                    <li>If the API encounters an internal server error, it should return a 500 Internal Server Error status.</li>
                 </b>
            </ul>
        </div>""",unsafe_allow_html=True)
    else:
        st.write("""
        Error Handling:
        <div style="padding-left: 20px;">
            <ul>
                <li>If the API is accessed with an invalid HTTP method (e.g., POST), it should return a 405 Method Not Allowed status.</li>
                <li>If the API encounters an internal server error, it should return a 500 Internal Server Error status.</li>
            </ul>
        </div>""",unsafe_allow_html=True)
    if st.toggle("Show Analysis", key="api_valid"):
        st.markdown("""
            <span style="color: rgb(255,75,75);">
                    This section on validation mentions that all fields in the response need to match their expected data types,
                    but as we identified in earlier analysis, most of the fields do not have their data types specified.
                    <br>It's good that we identified this earlier and will be querying this with the PO and team.
                    <br>
                    <br>Moving on, we can validate a valid URL for the image field, but our queries around knowing if the actual image is the correct one for each given product
                    and what behaviour is expected if no image is present are still valid.
                    <br>The info. about the ratings fields, reiterates the data types, and gives some more detail, but the specific's of how
                    and what we will actually be validating these values against still needs defining.
                <br>
            </span>
            """, unsafe_allow_html=True)
        st.write("""
            <b>Validation:</b>
            <div style="padding-left: 20px;">
                <ul>
                    <b>
                        <li>All fields in the response should match their expected data types.</li>
                        <li>The image field must contain a valid URL.</li>
                        <li>The rating.rate should be a float between 0.0 and 5.0.</li>
                        <li>The rating.count should be a non-negative integer.</li>
                    </b>
                </ul>
            </div>""", unsafe_allow_html=True)
    else:
        st.write("""
            Validation:
            <div style="padding-left: 20px;">
                <ul>
                    <li>All fields in the response should match their expected data types.</li>
                    <li>The image field must contain a valid URL.</li>
                    <li>The rating.rate should be a float between 0.0 and 5.0.</li>
                    <li>The rating.count should be a non-negative integer.</li>
                </ul>
            </div>                
            """
            ,unsafe_allow_html=True)
    if st.toggle("Show Analysis", key="api_perf"):
        st.markdown("""
            <span style="color: rgb(255,75,75);">
                    This section on validation mentions that all fields in the response need to match their expected data types,
                    but as we identified in earlier analysis, most of the fields do not have their data types specified.
                    <br>It's good that we identified this earlier and will be querying this with the PO and team.
                    <br>
                    <br>Moving on, we can validate a valid URL for the image field, but our queries around knowing if the actual image is the correct one for each given product
                    and what behaviour is expected if no image is present are still valid.
                    <br>The info. about the ratings fields, reiterates the data types, and gives some more detail, but the specific's of how
                    and what we will actually be validating these values against still needs defining.
                <br>
            </span>
            """, unsafe_allow_html=True)
        st.write("""
                <b>Performance:</b>
                <div style="padding-left: 20px;">
                    <ul>
                        <b>
                            <li>The API should respond within 2 seconds under normal load conditions.</li>
                        </b>
                    </ul>
                </div>
                """
                ,unsafe_allow_html=True)
    else:
        st.write("""
                Performance:
                <div style="padding-left: 20px;">
                    <ul>
                        <li>The API should respond within 2 seconds under normal load conditions.</li>
                    </ul>
                </div>
                """
                ,unsafe_allow_html=True)

def api_page_four():
    st.header("Static Testing the User Story")
    st.subheader("The Product Owner's Response:")
    st.markdown("""
    > Thank you for the detailed analysis. Here are my clarifications and responses to your queries: <br><br>

    <ul>
        <li>The term "user" in the original story refers to <strong>developers building client applications</strong> that consume this API.</li>
        <li>The "view and analyze product information" means displaying the data in a UI and providing options for developers to manipulate 
        or export it for deeper analysis, such as generating reports.
        </li>
    </ul>

    <strong>Specific responses:</strong><br>

    <ul>
        <li><strong>Product ID</strong>: Alphanumeric, max length 50 characters.</li>
        <li><strong>Title</strong>: Mandatory, max 255 characters.</li>
        <li><strong>Description</strong>: Optional, no character limit but ideally under 1,000 characters for performance.</li>
        <li><strong>Category</strong>: Mandatory, limited to predefined values (e.g., Electronics, Home).</li>
        <li><strong>Image URL</strong>: Validate that it is a proper URL; use a placeholder for invalid or missing images.</li>
        <li><strong>Rating fields</strong>: 
            <ul>
                <li><code>rate</code> should default to <code>null</code> if no ratings exist.</li>
                <li><code>count</code> defaults to <code>0</code>.</li>
            </ul>
        </li>
    </ul>

    <ul>
        <li>For error messages, include timestamps, a unique request ID, and error details in JSON format for both 405 and 500 errors.</li>
        <li>If the product list is empty, return a 200 status with an empty array.</li>
        <li>Regarding "analyse product details," no specific format is required for analysis tools, but ensure data is consistently structured 
        and accurate.
        </li>
    </ul>
    The Product owner also arranges to give me access to the database, as well as providing a list of images and to which Product's they belong.
    """, unsafe_allow_html=True)

def api_page_five():
    st.header("Static Testing the User Story")
    st.subheader("The Rewritten user Story")
    st.write("Following the Product Owner's responses the user story is rewritten to accurately reflect the solution that needs to be built"
             "and the testing that needs to be done.")
    st.markdown("""
    > **User Story Statement:**<br>  
    As a developer building client applications, I want to retrieve product details via an API so that I can display and analyze product information in the UI and support further data manipulation or reporting.  

    **Detailed Description:**<br>  
    The system will provide an API endpoint: <code>/products</code> that returns a list of products. Each product will include the following details:  

    <ul>
        <li><strong>Product ID</strong>: Alphanumeric, max length 50 characters.</li>
        <li><strong>Title</strong>: Mandatory, max 255 characters.</li>
        <li><strong>Price</strong>: Decimal value representing the product's price.</li>
        <li><strong>Description</strong>: Optional, no character limit but ideally under 1,000 characters for performance.</li>
        <li><strong>Category</strong>: Mandatory, limited to predefined values (e.g., Electronics, Home).</li>
        <li><strong>Image URL</strong>: Must be a valid URL. If invalid or missing, return a placeholder image.</li>
        <li><strong>Rating Information:</strong>  
            <ul>
                <li><code>rate</code> (float): The average rating. Defaults to <code>null</code> if no ratings exist.</li>
                <li><code>count</code> (integer): The number of ratings. Defaults to <code>0</code>.</li>
            </ul>
        </li>
    </ul>

    This data will be consumed by client applications for UI display or for additional analysis by developers.<br><br>

    **Acceptance Criteria:**<br>  

    <ul>
        <li>When a GET request is sent to <code>/products</code>, the API should return a <code>200 OK</code> status.</li>
        <li>The response body should contain a JSON array of products with the fields defined above.</li>
        <li>If the product list is empty, the response should include a <code>200 OK</code> status with an empty array.</li>
        <li>If an invalid HTTP method (e.g., POST) is used, return a <code>405 Method Not Allowed</code> status with error details (timestamp, request ID, message).</li>
        <li>If an internal server error occurs, return a <code>500 Internal Server Error</code> status with error details (timestamp, request ID, message).</li>
    </ul>

    **Validation:**<br>  

    <ul>
        <li>All fields in the response should match their expected data types.</li>
        <li>The <code>image</code> field must contain a valid URL.</li>
        <li>The <code>rating.rate</code> should be a float between <code>0.0</code> and <code>5.0</code>.</li>
        <li>The <code>rating.count</code> should be a non-negative integer.</li>
    </ul>

    **Performance:**<br>  
    <ul>
        <li>The API should respond within 2 seconds under normal load conditions.</li>
    </ul>
    """,unsafe_allow_html=True)

def api_page_six():
    st.header("Static Testing the User Story")
    st.subheader("Writing Tests")
    st.write("""Now we have a User Story that is accurate. We have all the information we need, we can write clear and concise tests.
             In addition to the summarised test's below. I would investigate the database to identify the main tables involved in the
             Product and Rating process and write queries to accurately calculate the ratings for the Products I expect to be returned.
             This would give me expected values to validate the rating values against.""")
    st.markdown("""
    ### Functional Test Cases
    <ul>
        <li><strong>Verify successful response with products:</strong><br>
            <strong>Input:</strong> Send a valid `GET` request to `/products`.<br>
            <strong>Expected Result:</strong><br>
            - API returns `200 OK`.<br>
            - Response contains a JSON array of products with all fields (Product ID, Title, Price, Description, Category, Image URL, Rating Information).
        </li>
        <li><strong>Verify response when product list is empty:</strong><br>
            <strong>Input:</strong> Send a valid `GET` request to `/products` when no products exist.<br>
            <strong>Expected Result:</strong><br>
            - API returns `200 OK`.<br>
            - Response contains an empty array (`[]`).
        </li>
        <li><strong>Verify required fields are returned:</strong><br>
            <strong>Input:</strong> Send a valid `GET` request to `/products`.<br>
            <strong>Expected Result:</strong><br>
            - All mandatory fields (Product ID, Title, Price, Category) are present and not null.
        </li>
        <li><strong>Verify optional fields behavior:</strong><br>
            <strong>Input:</strong> Send a valid `GET` request to `/products` with some products missing `Description` or `Image URL`.<br>
            <strong>Expected Result:</strong><br>
            - Missing `Description` is either empty or null.<br>
            - Missing or invalid `Image URL` is replaced by a placeholder.
        </li>
        <li><strong>Verify rating information defaults:</strong><br>
            <strong>Input:</strong> Send a valid `GET` request to `/products` with products having no ratings.<br>
            <strong>Expected Result:</strong><br>
            - `rating.rate` defaults to `null`.<br>
            - `rating.count` defaults to `0`.
        </li>
        <li><strong>Verify handling of invalid HTTP methods:</strong><br>
            <strong>Input:</strong> Send a `POST` request to `/products`.<br>
            <strong>Expected Result:</strong><br>
            - API returns `405 Method Not Allowed`.<br>
            - Error message includes timestamp, request ID, and error description.
        </li>
        <li><strong>Verify handling of internal server errors:</strong><br>
            <strong>Input:</strong> Simulate a server-side error during a `GET` request to `/products`.<br>
            <strong>Expected Result:</strong><br>
            - API returns `500 Internal Server Error`.<br>
            - Error message includes timestamp, request ID, and error description.
        </li>
        <li><strong>Verify valid product data types:</strong><br>
            <strong>Input:</strong> Send a valid `GET` request to `/products`.<br>
            <strong>Expected Result:</strong><br>
            - Product ID is alphanumeric.<br>
            - Title is a string with a max length of 255 characters.<br>
            - Price is a decimal.<br>
            - Rating information has `rate` as a float between `0.0` and `5.0` and `count` as a non-negative integer.
        </li>
    </ul>

    ### Performance Test Cases
    <ul>
        <li><strong>Verify response time under normal load:</strong><br>
            <strong>Input:</strong> Send a valid `GET` request to `/products` under normal load conditions.<br>
            <strong>Expected Result:</strong><br>
            - API responds within 2 seconds.
        </li>
        <li><strong>Verify response time under heavy load:</strong><br>
            <strong>Input:</strong> Send a valid `GET` request to `/products` under heavy load conditions (e.g., high concurrent users).<br>
            <strong>Expected Result:</strong><br>
            - API responds within acceptable performance thresholds.
        </li>
    </ul>

    ### Validation Test Cases
    <ul>
        <li><strong>Verify valid image URLs:</strong><br>
            <strong>Input:</strong> Send a valid `GET` request to `/products` with products having valid and invalid image URLs.<br>
            <strong>Expected Result:</strong><br>
            - Valid URLs return images successfully.<br>
            - Invalid URLs return a placeholder.
        </li>
        <li><strong>Verify field validation:</strong><br>
            <strong>Input:</strong> Send a valid `GET` request to `/products` and verify the response data types.<br>
            <strong>Expected Result:</strong><br>
            - All fields match their specified data types.
        </li>
    </ul>

    ### Negative Test Cases
    <ul>
        <li><strong>Verify invalid product IDs:</strong><br>
            <strong>Input:</strong> Test with products containing invalid Product IDs (e.g., too long, non-alphanumeric).<br>
            <strong>Expected Result:</strong><br>
            - API rejects invalid data and logs errors (if applicable).
        </li>
        <li><strong>Verify malformed requests:</strong><br>
            <strong>Input:</strong> Send malformed or incomplete requests to `/products`.<br>
            <strong>Expected Result:</strong><br>
            - API returns appropriate error responses (`400 Bad Request` or similar).
        </li>
    </ul>
    """, unsafe_allow_html=True)



