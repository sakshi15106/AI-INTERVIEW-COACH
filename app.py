
import streamlit as st
import time
import re

st.set_page_config(page_title="AI Interview Coach", page_icon="🎯", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "home"
if "name" not in st.session_state:
    st.session_state.name = ""
if "role" not in st.session_state:
    st.session_state.role = "Python Developer"
if "index" not in st.session_state:
    st.session_state.index = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

role_questions = {
    "Python Developer": [
        ("What is Python?", "Python is a high-level interpreted programming language known for its simple syntax."),
        ("What are the features of Python?", "Python is easy to learn, interpreted, portable, object-oriented, and has many libraries."),
        ("What is a list in Python?", "A list is an ordered and changeable collection of items in Python.")
    ],
    "Data Analyst": [
        ("What is Data Analysis?", "Data analysis is the process of collecting, cleaning, transforming, and interpreting data."),
        ("What is a dataset?", "A dataset is a collection of related data organized in rows and columns."),
        ("What is data visualization?", "Data visualization presents data through charts, graphs, and other visual formats.")
    ],
    "AI/ML Engineer": [
        ("What is Artificial Intelligence?", "Artificial Intelligence enables computers to perform tasks that normally require human intelligence."),
        ("What is Machine Learning?", "Machine Learning is a branch of AI that allows computers to learn patterns from data."),
        ("What is a training dataset?", "A training dataset is data used to teach a machine learning model to identify patterns.")
    ]
}

def calculate_score(user_answer, sample_answer):
    sample = set(re.findall(r"\b[a-z0-9]+\b", sample_answer.lower()))
    user = set(re.findall(r"\b[a-z0-9]+\b", user_answer.lower()))
    return min(10, round(len(sample & user) / max(len(sample), 1) * 10))

# HOME DASHBOARD
if st.session_state.page == "home":
    st.title("🎯 AI Interview Coach")
    st.subheader("Your Personal Interview Preparation Dashboard")
    st.write("Practice interview questions and improve your confidence!")

    st.divider()
    st.subheader("👤 Student Details")

    st.session_state.name = st.text_input("Enter Your Name", value=st.session_state.name)

    st.subheader("💼 Select Interview Role")
    st.session_state.role = st.selectbox(
        "Choose your job role",
        list(role_questions.keys()),
        index=list(role_questions.keys()).index(st.session_state.role)
    )

    st.divider()
    st.subheader("📊 Dashboard Overview")
    c1, c2, c3 = st.columns(3)
    c1.metric("Job Roles", "3")
    c2.metric("Questions", "9")
    c3.metric("Time", "60 sec")

    st.divider()
    st.subheader("🚀 Start Your Practice")

    if st.button("Start Interview ▶", type="primary", use_container_width=True):
        if not st.session_state.name.strip():
            st.warning("Please enter your name first.")
        else:
            st.session_state.index = 0
            st.session_state.page = "interview"
            st.rerun()

    with st.expander("ℹ️ About This Project"):
        st.write("AI Interview Coach is a Python and Streamlit based interview practice application. It provides role-based questions, a countdown timer, sample answers and keyword-based scoring.")

    st.caption("AI Interview Coach | Developed using Python and Streamlit")

# INTERVIEW PAGE
else:
    role = st.session_state.role
    questions = role_questions[role]
    index = st.session_state.index
    question, sample_answer = questions[index]

    st.title("🎯 Interview Practice")
    st.write(f"Welcome, {st.session_state.name}!")

    if st.button("🏠 Home Dashboard"):
        st.session_state.page = "home"
        st.rerun()

    st.divider()
    st.subheader(f"Role: {role}")
    st.subheader(f"Question {index + 1} of {len(questions)}")
    st.progress((index + 1) / len(questions))
    st.write(question)

    timer_key = f"{role}_{index}"
    answer_key = f"answer_{role}_{index}"

    if st.session_state.get("timer_key") != timer_key:
        st.session_state.timer_key = timer_key
        st.session_state.timer_start = time.time()
        st.session_state.time_up = False
        st.session_state.timer_score = None

    if answer_key not in st.session_state:
        st.session_state[answer_key] = st.session_state.answers.get(timer_key, "")

    @st.fragment(run_every="1s")
    def show_timer():
        remaining = max(0, 60 - int(time.time() - st.session_state.timer_start))
        if remaining > 0:
            st.info(f"⏱️ Time Remaining: {remaining} seconds")
        else:
            st.error("⏰ Time Up!")
            if not st.session_state.time_up:
                st.session_state.time_up = True
                saved_answer = st.session_state.get(answer_key, "")
                st.session_state.answers[timer_key] = saved_answer
                st.session_state.timer_score = calculate_score(saved_answer, sample_answer)
                st.rerun(scope="app")

    show_timer()

    answer = st.text_area(
        "Write your answer here",
        key=answer_key,
        disabled=st.session_state.time_up
    )

    if st.session_state.time_up:
        st.warning(f"Time is up! Your Score: {st.session_state.timer_score}/10")

    if st.button("Check My Answer", type="primary", disabled=st.session_state.time_up):
        st.session_state.answers[timer_key] = answer
        if len(answer.strip().split()) < 5:
            st.warning("Please write a more detailed answer.")
        else:
            score = calculate_score(answer, sample_answer)
            st.success(f"Your Score: {score}/10")
            if score >= 7:
                st.success("Excellent! Good answer.")
            elif score >= 4:
                st.info("Good effort! Keep improving.")
            else:
                st.warning("Keep practising!")

    if st.button("Show Sample Answer"):
        st.info(sample_answer)

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Previous", disabled=(index == 0)):
            st.session_state.answers[timer_key] = answer
            st.session_state.index -= 1
            st.rerun()

    with col2:
        if index < len(questions) - 1:
            if st.button("Next Question ➡"):
                st.session_state.answers[timer_key] = answer
                st.session_state.index += 1
                st.rerun()
        else:
            if st.button("Finish Interview 🏁"):
                st.session_state.answers[timer_key] = answer
                st.session_state.page = "home"
                st.rerun()

    st.caption("AI Interview Coach | Interview Practice")
