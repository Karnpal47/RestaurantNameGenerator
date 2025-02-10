import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")

cuisine=st.sidebar.selectbox("Pickout your cuisine",["Indian","Arabic","Mexican","American"])
def restaurant_name_genearator(cuisine):
    return{
        "restaurant_name":"Arebic restro",
        "menu_items":"chicken tikka,Paneer masala"
    }
if cuisine:
    response=langchain_helper.restaurant_name_genearator(cuisine)
    
    st.header(response['restaurant_name'])
    menu_items=response['menu_items'].split(",")
    st.write("**Menu_items**")

    for item in menu_items:
        st.write("-",item)
