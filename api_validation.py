import streamlit as st
import requests
import json

def display_api_streamlit_elements():
    # App Title
    st.title("API Validation Tool")
    st.write("Test and validate any public API by entering its endpoint below.")

    # Input for API URL
    api_url = st.text_input("Enter API URL:", value="https://fakestoreapi.com/products")

    # Button to trigger the API call
    if st.button("Test API"):
        if api_url:
            try:
                # Send a GET request
                with st.spinner("Sending request..."):
                    response = requests.get(api_url)

                # Display basic information
                st.subheader("Response Details:")
                st.write(f"**Status Code:** {response.status_code}")
                st.write(f"**Response Time:** {response.elapsed.total_seconds()} seconds")

                # Try to parse JSON response
                try:
                    response_json = response.json()
                    st.subheader("JSON Response:")
                    st.json(response_json)
                except json.JSONDecodeError:
                    st.subheader("Response Text:")
                    st.text(response.text)

            except requests.RequestException as e:
                st.error(f"Error occurred: {e}")
        else:
            st.warning("Please enter a valid API URL.")
