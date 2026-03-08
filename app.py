import streamlit as st

st.title("🎓 Student Profile Builder")

st.write("Welcome! This is my Streamlit UI Assignment.")

name = st.text_input("Enter your name")

age = st.number_input("Enter your age", 1, 100)

course = st.selectbox(
    "Select your course",
    ["BSIT", "BSCS", "BSIS"]
)

if st.button("Submit"):
    st.success("Form submitted!")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Course:", course)
