
import streamlit as st
import time
import re

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🎯",
    layout="centered"
)

# ---------------- SESSION STATE ----------------

defaults = {
    "page": "home",
    "name": "",
    "role": "Python Developer",
    "index": 0,
    "answers": {},
    "scores": {},
    "timer_start": None,
    "timer_key": None,
    "time_up": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ---------------- INTERVIEW QUESTIONS ----------------

role_questions = {

    "Python Developer": [

        ("What is Python?",
         "Python is a high-level interpreted programming language known for its simple syntax."),

        ("What are the features of Python?",
         "Python is easy to learn, interpreted, portable, object-oriented and has many libraries."),

        ("What is a list in Python?",
         "A list is an ordered and changeable collection of items in Python."),

        ("What is a tuple?",
         "A tuple is an ordered and immutable collection of elements in Python."),

        ("What is a dictionary?",
         "A dictionary stores data in key value pairs and is mutable in Python."),

        ("What is a variable?",
         "A variable is a named memory location used to store data values in Python."),

        ("What is a function?",
         "A function is a reusable block of code that performs a specific task."),

        ("What is a loop?",
         "A loop is used to execute a block of code repeatedly in Python."),

        ("What is OOP?",
         "Object oriented programming is a programming approach based on classes and objects."),

        ("What is exception handling?",
         "Exception handling manages runtime errors using try, except, else and finally blocks.")
    ],

    "Data Analyst": [

        ("What is Data Analysis?",
         "Data analysis is the process of collecting, cleaning, transforming and interpreting data."),

        ("What is a dataset?",
         "A dataset is a collection of related data organized in rows and columns."),

        ("What is data visualization?",
         "Data visualization presents data through charts, graphs and other visual formats."),

        ("What is data cleaning?",
         "Data cleaning is the process of correcting missing, duplicate and incorrect data."),

        ("What is Microsoft Excel?",
         "Microsoft Excel is a spreadsheet application used to organize, calculate and analyze data."),

        ("What is SQL?",
         "SQL is a structured query language used to manage and retrieve data from databases."),

        ("What is a database?",
         "A database is an organized collection of data that can be stored and accessed electronically."),

        ("What is Python used for in data analysis?",
         "Python is used for data cleaning, analysis and visualization with libraries such as Pandas and NumPy."),

        ("What is a bar chart?",
         "A bar chart represents categorical data using rectangular bars to compare values."),

        ("What is a KPI?",
         "A Key Performance Indicator is a measurable value used to evaluate business performance.")
    ],

    "AI/ML Engineer": [

        ("What is Artificial Intelligence?",
         "Artificial Intelligence enables computers to perform tasks that normally require human intelligence."),

        ("What is Machine Learning?",
         "Machine Learning is a branch of AI that allows computers to learn patterns from data."),

        ("What is a training dataset?",
         "A training dataset is data used to teach a machine learning model to identify patterns."),

        ("What is Deep Learning?",
         "Deep Learning is a branch of machine learning that uses neural networks with multiple layers."),

        ("What is supervised learning?",
         "Supervised learning trains a model using labeled data containing inputs and correct outputs."),

        ("What is unsupervised learning?",
         "Unsupervised learning finds hidden patterns and groups in unlabeled data."),

        ("What is a neural network?",
         "A neural network is a computing model inspired by the human brain and made of connected neurons."),

        ("What is a classification algorithm?",
         "Classification is a machine learning technique used to predict categories or class labels."),

        ("What is overfitting?",
         "Overfitting occurs when a model learns training data too closely and performs poorly on new data."),

        ("What is model accuracy?",
         "Model accuracy measures the proportion of correct predictions made by a classification model.")
    ]
}

# ---------------- SCORING FUNCTION ----------------

def calculate_score(user_answer, sample_answer):

    sample_words = set(
        re.findall(r"\b[a-z0-9]+\b", sample_answer.lower())
    )

    user_words = set(
        re.findall(r"\b[a-z0-9]+\b", user_answer.lower())
    )

    if not sample_words:
        return 0

    score = len(sample_words & user_words) / len(sample_words) * 10

    return min(10, round(score))


# ---------------- RESET FUNCTION ----------------

def reset_interview():

    st.session_state.index = 0
    st.session_state.answers = {}
    st.session_state.scores = {}
    st.session_state.timer_start = None
    st.session_state.timer_key = None
    st.session_state.time_up = False


# ==================================================
#                    HOME DASHBOARD
# ==================================================

if st.session_state.page == "home":

    st.title("🎯 AI Interview Coach")

    st.subheader("Your Personal Interview Preparation Dashboard")

    st.write(
        "Practice interview questions and improve your confidence!"
    )

    st.divider()

    st.subheader("👤 Student Details")

    st.session_state.name = st.text_input(
        "Enter Your Name",
        value=st.session_state.name
    )

    st.subheader("💼 Select Interview Role")

    st.session_state.role = st.selectbox(
        "Choose your job role",
        list(role_questions.keys())
    )

    st.divider()

    st.subheader("📊 Dashboard Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric("Job Roles", "3")
    c2.metric("Total Questions", "30")
    c3.metric("Time", "60 sec")

    st.divider()

    st.subheader("🚀 Start Your Practice")

    if st.button(
        "Start Interview ▶",
        type="primary",
        use_container_width=True
    ):

        if not st.session_state.name.strip():

            st.warning("Please enter your name first.")

        else:

            reset_interview()

            st.session_state.page = "interview"

            st.rerun()

    with st.expander("ℹ️ About This Project"):

        st.write(
            "AI Interview Coach is a Python and Streamlit based "
            "interview practice application. It provides role-based "
            "questions, a countdown timer, sample answers and "
            "keyword-based scoring."
        )

    st.caption(
        "AI Interview Coach | Developed using Python and Streamlit"
    )


# ==================================================
#                    INTERVIEW PAGE
# ==================================================

elif st.session_state.page == "interview":

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

    st.subheader(
        f"Question {index + 1} of {len(questions)}"
    )

    st.progress(
        (index + 1) / len(questions)
    )

    st.markdown(f"### {question}")

    timer_key = f"{role}_{index}"

    answer_key = f"answer_{role}_{index}"

    if st.session_state.timer_key != timer_key:

        st.session_state.timer_key = timer_key

        st.session_state.timer_start = time.time()

        st.session_state.time_up = False

    if answer_key not in st.session_state:

        st.session_state[answer_key] = st.session_state.answers.get(
            timer_key, ""
        )

    # COUNTDOWN TIMER

    @st.fragment(run_every="1s")
    def show_timer():

        remaining = max(
            0,
            60 - int(time.time() - st.session_state.timer_start)
        )

        if remaining > 0:

            st.info(
                f"⏱️ Time Remaining: {remaining} seconds"
            )

        else:

            st.error("⏰ Time Up!")

            if not st.session_state.time_up:

                st.session_state.time_up = True

                saved_answer = st.session_state.get(
                    answer_key, ""
                )

                st.session_state.answers[timer_key] = saved_answer

                st.session_state.scores[timer_key] = calculate_score(
                    saved_answer, sample_answer
                )

                st.rerun(scope="app")

    show_timer()

    # ANSWER INPUT

    answer = st.text_area(
        "✍️ Write your answer here",
        key=answer_key,
        disabled=st.session_state.time_up
    )

    if st.session_state.time_up:

        st.warning(
            f"Time is up! Your Score: "
            f"{st.session_state.scores.get(timer_key, 0)}/10"
        )

    # CHECK ANSWER

    if st.button(
        "Check My Answer",
        type="primary",
        disabled=st.session_state.time_up
    ):

        st.session_state.answers[timer_key] = answer

        if len(answer.strip().split()) < 5:

            st.warning(
                "Please write a more detailed answer."
            )

        else:

            score = calculate_score(
                answer, sample_answer
            )

            st.session_state.scores[timer_key] = score

            st.success(
                f"Your Score: {score}/10"
            )

            if score >= 7:

                st.success(
                    "Excellent! Good answer."
                )

            elif score >= 4:

                st.info(
                    "Good effort! Keep improving."
                )

            else:

                st.warning(
                    "Keep practising!"
                )

    # SAMPLE ANSWER

    if st.button("Show Sample Answer"):

        st.info(sample_answer)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "⬅ Previous",
            disabled=(index == 0)
        ):

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

                if timer_key not in st.session_state.scores:

                    st.session_state.scores[timer_key] = calculate_score(
                        answer, sample_answer
                    )

                st.session_state.page = "result"

                st.rerun()

    st.caption(
        "AI Interview Coach | Interview Practice"
    )


# ==================================================
#                    RESULT PAGE
# ==================================================

elif st.session_state.page == "result":

    st.title("🏆 Interview Completed!")

    st.success(
        f"Congratulations, {st.session_state.name}!"
    )

    role = st.session_state.role

    questions = role_questions[role]

    total_score = sum(
        st.session_state.scores.get(
            f"{role}_{i}", 0
        )
        for i in range(len(questions))
    )

    maximum_score = len(questions) * 10

    st.metric(
        "Total Score",
        f"{total_score}/{maximum_score}"
    )

    st.subheader("📊 Performance Summary")

    for i, (question, sample) in enumerate(questions):

        score = st.session_state.scores.get(
            f"{role}_{i}", 0
        )

        st.write(
            f"**Question {i + 1}: {question}**"
        )

        st.write(
            f"Score: {score}/10"
        )

        st.progress(score / 10)

    percentage = round(
        total_score / maximum_score * 100
    )

    st.subheader(
        f"Overall Performance: {percentage}%"
    )

    if percentage >= 70:

        st.success(
            "Excellent performance! Keep it up."
        )

    elif percentage >= 40:

        st.info(
            "Good effort! More practice will help."
        )

    else:

        st.warning(
            "Keep practising to improve your performance."
        )

    st.divider()

    if st.button(
        "🔄 Start New Interview",
        type="primary",
        use_container_width=True
    ):

        reset_interview()

        st.session_state.page = "home"

        st.rerun()

    st.caption(
        "AI Interview Coach | Thank you for practising!"
    )
