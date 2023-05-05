import streamlit as st
import pandas


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("venv/Utkarsh.png")

with col2:
    st.title("Utkarsh Bhardwaj")
    content = """
    Hi , I am Utkarsh , I am a Cloud Consultant who specializes in multiple cloud including GCP , AWS and Azure with GCP PCA & AWS SAA Certifications. 
    I have experience on developing mobile application using Flutter & Firebase and I have also written a book on Flutter.
    I have experience on UX Design using Figma.
    I am also a FinOps Certified Practitioner.
    I am also certified on Python."""

    st.info(content)

content2 = """
"Below you can find some of the app I have built using Python.Please feel free to contact me.Thanks!!"""
row1 = st.write(content2)

col3, empty_col, col4 = st.columns([2, 1, 2])

df = pandas.read_csv("venv/data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("venv/images/" + row["image"])
        st.write(f"[Source Code] {row['url']}")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("venv/images/" + row["image"])
        st.write(f"Source Code: {row['url']}")
