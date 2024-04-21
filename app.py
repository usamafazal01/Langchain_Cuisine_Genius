import streamlit as st
import langchain_helper

st.title('Restaurant Name Generator ')

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Chinese", "Italian", "Mexican", "Indian", "Japanese", "French", "Thai", "Greek", "Spanish", "Vietnamese", "Korean", "Mediterranean", "American", "Brazilian", "Turkish", "Lebanese", "German", "British", "Russian", "Moroccan"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())

    # Split menu items by newline and remove any leading/trailing spaces
    menu_items = []
    for item in response['menu_items'].strip().split("\n"):
        # Check if the item contains a dot before splitting
        if ". " in item:
            menu_items.append(item.strip().split(". ", 1)[1])
        else:
            menu_items.append(item.strip())

    st.write("**Menu Items** ")
    for item in menu_items:
        # Display each item with a bullet point
        st.write("-", item)
