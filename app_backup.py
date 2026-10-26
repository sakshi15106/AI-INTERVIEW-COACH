import streamlit as st

st.title("AI Interview Coach")
st.write("Welcome to AI Interview Coach!")

name = st.text_input("Enter your name")

role = st.selectbox(
    "Select your job role",
    ["Python Developer", "Data Analyst", "AI/ML Engineer"]
)

if name:
    st.write("Welcome", name)

st.write("Let's practice your interview!")
st.subheader("Interview Questions")

if role == "Python Developer":
    st.write("Question 1: What is Python?")
elif role == "Data Analyst":
    st.write("Question 1: What is Data Analysis?")
else:
    st.write("Question 1: What is Artificial Intelligence?")

answer = st.text_area("Write your answer here")

if answer:
    st.write("Your answer has been submitted!")
    
if st.button("Check My Answer"):
    if len(answer.strip()) >= 20:
        st.success("Good job! Your answer has enough detail.")
    elif answer.strip():
        st.warning("Please write a little more detail in your answer.")
    else:
        st.error("Please write your answer first.")

    
if st.button("Next Question"):
    st.write("Question 2: What are the features of Python?")
