import streamlit as st

def api_page_nav_buttons(current_page, max_page):
    # Add columns, for buttons to exist within.
    col1, col2 = st.columns([1, 1])

    with col1:
        if current_page > 1:
            if st.button("Previous Page"):
                set_page_as_read(current_page)
                # Decrease current page number when Previous page button is clicked
                st.session_state.api_current_project_page -= 1

                # Tell the session state that a navigation button has been clicked
                st.session_state.page_nav_button_clicked = True

                # Rerun the streamlit app, so that the page we have moved to is rendered.
                st.rerun()


    with col2:
        if current_page < max_page:
            if st.button("Next Page"):
                set_page_as_read(current_page)
                # Increase current page number when Next page button is clicked
                st.session_state.api_current_project_page += 1

                # Tell the session state that a navigation button has been clicked
                st.session_state.page_nav_button_clicked = True

                # Rerun the streamlit app, so that the page we have moved to is rendered.
                st.rerun()

def set_page_as_read(page):
    # Store the index adjusted value for the page before changes
    index_adjusted_page = page - 1

    # Mark the current page as being read before it's value is changed
    st.session_state.api_page_is_read[index_adjusted_page] = True


