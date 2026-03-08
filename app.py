import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Student Study Planner", layout="wide")

# SESSION STATE FOR LOGIN
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# LOGIN PAGE
if not st.session_state.logged_in:

    st.title("🔐 Student Study Planner Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "student" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")

# MAIN APP
else:

    # SIDEBAR
    st.sidebar.title("Navigation")

    page = st.sidebar.radio(
        "Go to",
        ["Home", "Study Planner", "Dashboard", "Feedback", "About"]
    )

    # THEME TOGGLE
    theme = st.sidebar.toggle("Dark Mode")

    if theme:
        st.markdown(
            """
            <style>
            body {
                background-color: #0E1117;
                color: white;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    st.sidebar.success("Logged in")

    # HOME PAGE
    if page == "Home":

        st.title("📚 Student Study Planner")

        st.header("Welcome!")

        st.write("This app helps students plan their study schedule.")

        st.image(
            "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
            width=500
        )

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

        st.balloons()

    # STUDY PLANNER
    elif page == "Study Planner":

        st.title("📝 Create Study Plan")

        name = st.text_input("Student Name")

        age = st.number_input("Age", 10, 60)

        gender = st.radio(
            "Gender",
            ["Male", "Female", "Other"]
        )

        course = st.selectbox(
            "Course",
            ["BSIT", "BSCS", "BSIS", "Data Science"]
        )

        subjects = st.multiselect(
            "Subjects",
            ["Programming", "Database", "Networking", "AI", "Math"]
        )

        study_hours = st.slider("Study Hours per Day", 1, 12)

        confidence = st.slider("Programming Confidence", 1, 10)

        birthday = st.date_input("Birthdate")

        study_time = st.time_input("Preferred Study Time")

        bio = st.text_area("Short Bio")

        color = st.color_picker("Favorite Color")

        upload = st.file_uploader("Upload Study File")

        agree = st.checkbox("I confirm the information is correct")

        if st.button("Generate Study Plan"):

            if agree:

                st.success("Study Plan Generated!")

                data = {
                    "Name": [name],
                    "Age": [age],
                    "Course": [course],
                    "Study Hours": [study_hours],
                    "Confidence": [confidence]
                }

                df = pd.DataFrame(data)

                st.write("### Student Summary")
                st.dataframe(df)

                # DOWNLOAD BUTTON
                csv = df.to_csv(index=False).encode("utf-8")

                st.download_button(
                    "📥 Download Report",
                    csv,
                    "study_report.csv",
                    "text/csv"
                )

            else:
                st.warning("Please confirm your information")

    # DASHBOARD
    elif page == "Dashboard":

        st.title("📊 Study Dashboard")

        col1, col2, col3 = st.columns(3)

        col1.metric("Users", "120")
        col2.metric("Avg Study Hours", "5")
        col3.metric("Completed Tasks", "340")

        data = pd.DataFrame({
            "Subject": ["Programming", "Database", "Networking", "AI"],
            "Hours": [5, 3, 4, 2]
        })

        st.bar_chart(data.set_index("Subject"))

        with st.expander("Study Tips"):
            st.write("""
            - Study daily
            - Practice coding
            - Review lessons
            """)

        tab1, tab2 = st.tabs(["Coding", "Motivation"])

        with tab1:
            st.write("Coding improves with practice.")

        with tab2:
            st.write("Consistency leads to mastery.")

    # FEEDBACK
    elif page == "Feedback":

        st.title("💬 Feedback")

        rating = st.slider("Rate this app", 1, 10)

        recommend = st.selectbox(
            "Would you recommend this app?",
            ["Yes", "Maybe", "No"]
        )

        comments = st.text_area("Comments")

        if st.button("Submit Feedback"):
            st.success("Thank you for your feedback!")

    # ABOUT
    elif page == "About":

        st.title("About This Application")

        st.subheader("What the App Does")
        st.write("""
        This application helps students organize and plan their study schedule
        while demonstrating various Streamlit UI components.
        """)

        st.subheader("Target Users")
        st.write("College students who want to manage their study time.")

        st.subheader("Inputs Collected")
        st.write("""
        - Name
        - Age
        - Gender
        - Course
        - Subjects
        - Study hours
        - Confidence level
        - Birthdate
        - Bio
        - Uploaded file
        """)

        st.subheader("Outputs")
        st.write("""
        The app generates a student study summary and downloadable report.
        """)
