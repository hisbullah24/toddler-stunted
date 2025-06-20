# streamlit_app.py
import streamlit as st
from navigation import render_sidebar
from page import Home, Dashboard, Dataset, Home2

#bar style chrome
st.set_page_config(page_title="Klasifikasi Gizi Balita", page_icon="🤱🏻", layout="centered")

# Sidebar & halaman yang dipilih
selected_page = render_sidebar()

# Routing berdasarkan pilihan di sidebar
if selected_page == "Home 1":
    Home.main()
elif selected_page == "Dashboard":
    Dashboard.main()
elif selected_page == "Dataset":
    Dataset.main()
elif selected_page == "Home 2":
    Home2.main()