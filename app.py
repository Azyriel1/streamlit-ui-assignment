import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Student Study Planner", layout="wide")

# SIDEBAR
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Study Planner", "Dashboard", "Feedback", "About"]
)

st.sidebar.info("Streamlit UI Components Demo App")

# HOME PAGE
if page == "Home":

    st.title("📚 Student Study Planner")
    st.header("Welcome to the Study Planner App")

    st.write("This app demonstrates many Streamlit UI components.")

    st.success("Use the sidebar to navigate through the app.")

    st.image(
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
        caption="Students studying together",
        width=500
    )

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    st.balloons()

# STUDY PLANNER PAGE
elif page == "Study Planner":

    st.title("📝 Create Your Study Plan")

    st.subheader("Student Information")

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
        "Subjects to Study",
        ["Programming", "Database", "Networking", "AI", "Math"]
    )

    study_hours = st.slider(
        "Daily Study Hours",
        1, 12
    )

    confidence = st.slider(
        "Programming Confidence",
        1, 10
    )

    birthday = st.date_input("Birthdate")

    study_time = st.time_input("Preferred Study Time")

    color = st.color_picker("Favorite Color")

    bio = st.text_area("Short Description About You")

    uploaded_file = st.file_uploader("Upload Study Notes")

    agree = st.checkbox("I confirm the information is correct")

    st.divider()

    if st.button("Generate Study Plan"):

        if agree:

            st.success("Study Plan Created!")

            st.write("### Student Summary")

            st.write("Name:", name)
            st.write("Age:", age)
            st.write("Gender:", gender)
            st.write("Course:", course)
            st.write("Subjects:", subjects)
            st.write("Study Hours:", study_hours)
            st.write("Confidence Level:", confidence)
            st.write("Preferred Study Time:", study_time)

            st.info("Stay consistent and practice daily!")

        else:

            st.warning("Please confirm your information first.")

# DASHBOARD PAGE
elif page == "Dashboard":

    st.title("📊 Study Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Students Using App", "120")
    col2.metric("Average Study Hours", "5")
    col3.metric("Assignments Completed", "340")

    st.divider()

    data = pd.DataFrame({
        "Subject": ["Programming", "Database", "Networking", "AI"],
        "Study Hours": [5, 3, 4, 2]
    })

    st.subheader("Study Time Distribution")

    st.bar_chart(data.set_index("Subject"))

    st.subheader("Data Table")

    st.dataframe(data)

    with st.expander("Study Tips"):

        st.write("""
        - Study consistently
        - Practice coding daily
        - Work on small projects
        - Review previous lessons
        """)

    tab1, tab2 = st.tabs(["Programming", "Motivation"])

    with tab1:
        st.write("Practice coding every day to improve your skills.")

    with tab2:
        st.write("Consistency is the key to success.")

# FEEDBACK PAGE
elif page == "Feedback":

    st.title("💬 App Feedback")

    rating = st.slider("Rate this app", 1, 10)

    recommend = st.selectbox(
        "Would you recommend this app?",
        ["Yes", "Maybe", "No"]
    )

    comments = st.text_area("Additional Comments")

    if st.button("Submit Feedback"):

        st.success("Thank you for your feedback!")

# ABOUT PAGE
elif page == "About":

    st.title("About This Application")

    st.subheader("What the App Does")

    st.write("""
    The Student Study Planner helps students organize their study habits.
    It collects information about the student and generates a simple study plan.
    """)

    st.subheader("Target Users")

    st.write("""
    The target users are college students who want to plan their daily study schedule.
    """)

    st.subheader("Inputs Collected")

    st.write("""
    - Student name
    - Age
    - Gender
    - Course
    - Subjects to study
    - Study hours
    - Programming confidence
    - Birthdate
    - Preferred study time
    - Bio description
    - Favorite color
    - Uploaded study file
    """)

    st.subheader("Outputs Displayed")

    st.write("""
    The application displays a summary of the student's information,
    a generated study plan, dashboard metrics, and study recommendations.
    """)
