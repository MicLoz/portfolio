import streamlit as st

#Colour picker function.
def colour_picker_section():
    # Colour pickers for customisation
    st.write("### Customise Theme Colours")
    background_color = st.color_picker("Pick a background colour", "#FFFFFF")
    text_color = st.color_picker("Pick a text colour", "#000000")

    return {
        "background_color": background_color,
        "text_color": text_color
    }

def return_custom_styling(theme_colours):
    return_value = f"""
        <style>
            .stApp {{
                background-color: {theme_colours['background_color']};
                color: {theme_colours['text_color']};
            }}
        </style>
    """
    return return_value