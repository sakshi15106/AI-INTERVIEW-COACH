
import streamlit as st

st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 AI Interview Coach")
st.write("Practice interview questions and improve your answers!")

name = st.text_input("Enter your name")

role_questions = {
    "Python Developer": [
        {
            "question": "What is Python?",
            "answer": "Python is a high-level, interpreted programming language known for its simple syntax."
        },
        {
            "question": "What are the features of Python?",
            "answer": "Python is easy to learn, interpreted, portable, object-oriented, and has many libraries."
        },
        {
            "question": "What is a list in Python?",
            "answer": "A list is an ordered and changeable collection of items in Python."
        }
    ],
    "Data Analyst": [
        {
            "question": "What is Data Analysis?",
            "answer": "Data analysis is the process of collecting, cleaning, transforming, and interpreting data."
        },
        {
            "question": "What is a dataset?",
            "answer": "A dataset is a collection of related data organized in rows and columns or another structure."
        },
        {
            "question": "What is data visualization?",
            "answer": "Data visualization presents data through charts, graphs, and other visual formats."
        }
    ],
    "AI/ML Engineer": [
        {
            "question": "What is Artificial Intelligence?",
            "answer": "Artificial Intelligence enables computers to perform tasks that normally require human intelligence."
        },
        {
            "question": "What is Machine Learning?",
            "answer": "Machine Learning is a branch of AI that allows computers to learn patterns from data."
        },
        {
            "question": "What is a training dataset?",
            "answer": "A training dataset is data used to teach a machine learning model to identify patterns."
        }
    ]
}

role = st.selectbox(
    "Select your job role",
    list(role_questions.keys())
)

questions = role_questions[role]

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

# Reset the question when the selected role changes
if "previous_role" not in st.session_state:
    st.session_state.previous_role = role

if st.session_state.previous_role != role:
    st.session_state.question_index = 0
    st.session_state.answers = {}
    st.session_state.previous_role = role

index = st.session_state.question_index
question = questions[index]

st.divider()

if name:
    st.subheader(f"Welcome, {name}!")

st.subheader(f"Question {index + 1} of {len(questions)}")
st.write(question["question"])

answer = st.text_area(
    "Write your answer here",
    value=st.session_state.answers.get(index, ""),
    key=f"answer_{role}_{index}"
)

if st.button("Check My Answer", type="primary"):
    st.session_state.answers[index] = answer
    words = answer.strip().split()

    if len(words) < 5:
        st.warning("Please write a more detailed answer.")
    else:
        st.success("Good effort! You have written an answer.")
        st.info(
            "Tip: Compare your answer with the sample answer below. "
            "This version checks answer length, not factual correctness."
        )

if st.button("Show Sample Answer"):
    st.info(question["answer"])

col1, col2 = st.columns(2)

with col1:
    if st.button("⬅ Previous", disabled=(index == 0)):
        st.session_state.answers[index] = answer
        st.session_state.question_index -= 1
        st.rerun()

with col2:
    if st.button(
        "Next Question ➡",
        disabled=(index == len(questions) - 1)
    ):
        st.session_state.answers[index] = answer
        st.session_state.question_index += 1
        st.rerun()

st.divider()
st.caption("AI Interview Coach | Interview practice project")
