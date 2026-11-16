
import streamlit as st
import time

st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🎯",
    layout="centered"
)

# ---------------- PROJECT DATA ----------------

roles = {
    "Python Developer": [
        ("What is Python?",
         "Python is a high-level, interpreted programming language. It is easy to learn and used in AI, ML and web development.",
         ["high-level", "interpreted", "programming", "easy", "language"]),

        ("What is a list in Python?",
         "A list is an ordered and mutable collection of elements. It allows duplicate values and uses square brackets.",
         ["ordered", "mutable", "collection", "duplicate", "brackets"]),

        ("What is a tuple?",
         "A tuple is an ordered and immutable collection of elements. It is created using parentheses.",
         ["ordered", "immutable", "collection", "parentheses"]),

        ("What is a dictionary?",
         "A dictionary stores data in key-value pairs. It is mutable and uses unique keys.",
         ["key", "value", "pairs", "mutable", "unique"]),

        ("What is a variable?",
         "A variable is a name used to store data values in a program.",
         ["name", "store", "data", "values"]),

        ("What is a function?",
         "A function is a reusable block of code defined using the def keyword.",
         ["reusable", "block", "code", "def", "task"]),

        ("What is a loop?",
         "A loop executes a block of code repeatedly. Python has for and while loops.",
         ["repeatedly", "for", "while", "code"]),

        ("What is OOP?",
         "OOP stands for Object-Oriented Programming. It is based on classes and objects.",
         ["object", "oriented", "programming", "classes", "objects"]),

        ("What is exception handling?",
         "Exception handling manages runtime errors using try, except, else and finally blocks.",
         ["errors", "try", "except", "finally", "runtime"]),

        ("What is inheritance?",
         "Inheritance allows one class to acquire the properties and methods of another class.",
         ["class", "properties", "methods", "inheritance", "parent"])
    ],

    "Data Analyst": [
        ("What is Data Analysis?",
         "Data Analysis is the process of collecting, cleaning and examining data to find useful information.",
         ["collecting", "cleaning", "examining", "data", "information"]),

        ("What is a dataset?",
         "A dataset is a collection of related data organized in rows and columns.",
         ["collection", "data", "rows", "columns"]),

        ("What is Excel?",
         "Excel is spreadsheet software used for calculations, data organization and analysis.",
         ["spreadsheet", "software", "calculations", "analysis"]),

        ("What is Python used for in Data Analysis?",
         "Python is used for data cleaning, processing, visualization and analysis.",
         ["cleaning", "processing", "visualization", "analysis"]),

        ("What is Pandas?",
         "Pandas is a Python library used for data manipulation and analysis.",
         ["python", "library", "data", "manipulation", "analysis"]),

        ("What is NumPy?",
         "NumPy is a Python library used for numerical computing and working with arrays.",
         ["python", "library", "numerical", "computing", "arrays"]),

        ("What is data visualization?",
         "Data visualization is the graphical representation of data using charts and graphs.",
         ["graphical", "representation", "charts", "graphs", "data"]),

        ("What is SQL?",
         "SQL stands for Structured Query Language. It is used to manage and retrieve database data.",
         ["structured", "query", "language", "database", "data"]),

        ("What is a bar chart?",
         "A bar chart represents data using rectangular bars to compare different categories.",
         ["chart", "data", "bars", "compare", "categories"]),

        ("What is missing data?",
         "Missing data refers to values that are not available in a dataset. It can be handled by removing or filling values.",
         ["values", "dataset", "removing", "filling", "data"])
    ],

    "AI/ML Engineer": [
        ("What is Artificial Intelligence?",
         "Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence.",
         ["machines", "human", "intelligence", "tasks"]),

        ("What is Machine Learning?",
         "Machine Learning is a branch of AI that enables computers to learn from data.",
         ["branch", "AI", "computers", "learn", "data"]),

        ("What is Deep Learning?",
         "Deep Learning is a part of Machine Learning that uses neural networks with multiple layers.",
         ["machine", "learning", "neural", "networks", "layers"]),

        ("What is a neural network?",
         "A neural network is a computing model inspired by the human brain.",
         ["computing", "model", "human", "brain"]),

        ("What is supervised learning?",
         "Supervised learning trains a model using labelled data.",
         ["model", "labelled", "data", "training"]),

        ("What is unsupervised learning?",
         "Unsupervised learning finds patterns in data without labelled outputs.",
         ["patterns", "data", "without", "labelled"]),

        ("What is a dataset in Machine Learning?",
         "A dataset is a collection of examples used to train and test a machine learning model.",
         ["collection", "examples", "train", "test", "model"]),

        ("What is classification?",
         "Classification is a supervised learning technique used to predict categories or classes.",
         ["supervised", "learning", "predict", "categories", "classes"]),

        ("What is regression?",
         "Regression is a machine learning technique used to predict continuous numerical values.",
         ["machine", "learning", "predict", "continuous", "values"]),

        ("What is overfitting?",
         "Overfitting happens when a model learns training data too closely and performs poorly on new data.",
         ["model", "training", "data", "poorly", "new"])
    ]
}

# ---------------- SESSION STATE ----------------

defaults = {
    "started": False,
    "completed": False,
    "question_index": 0,
    "scores": {},
    "answers": {},
    "submitted": False,
    "timer_start": None,
    "time_up": False,
    "previous_role": None
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ---------------- HEADER ----------------

st.title("🎯 AI Interview Coach")
st.subheader("Your Personal Interview Preparation Dashboard")
st.write("Practice interview questions and improve your confidence!")

st.divider()

# ---------------- STUDENT DETAILS ----------------

if not st.session_state.started:

    st.header("👤 Student Details")

    name = st.text_input("Enter your name")

    st.header("💼 Select Interview Role")

    role = st.selectbox(
        "Choose your job role",
        list(roles.keys())
    )

    st.divider()

    st.header("📊 Dashboard Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric("Job Roles", "3")
    c2.metric("Questions", "30")
    c3.metric("Time", "60 sec")

    st.divider()

    st.header("🚀 Start Your Practice")

    if st.button("Start Your Practice", type="primary"):

        if not name.strip():
            st.warning("Please enter your name first.")

        else:
            st.session_state.student_name = name
            st.session_state.role = role
            st.session_state.started = True
            st.session_state.completed = False
            st.session_state.question_index = 0
            st.session_state.scores = {}
            st.session_state.answers = {}
            st.session_state.submitted = False
            st.session_state.time_up = False
            st.session_state.timer_start = time.time()

            st.rerun()

    st.divider()

    st.info(
        "About This Project\n\n"
        "AI Interview Coach is a Python and Streamlit based "
        "interview practice application. It provides role-based "
        "questions, a countdown timer, sample answers and "
        "keyword-based scoring."
    )

    st.caption("AI Interview Coach | Developed using Python and Streamlit")

# ---------------- INTERVIEW SCREEN ----------------

elif st.session_state.started and not st.session_state.completed:

    role = st.session_state.role
    index = st.session_state.question_index
    questions = roles[role]

    question, sample, keywords = questions[index]

    st.success(
        f"Welcome {st.session_state.student_name}!"
    )

    st.subheader(f"Role: {role}")

    st.progress((index + 1) / len(questions))

    st.markdown(
        f"### Question {index + 1} of {len(questions)}"
    )

    st.header(question)

    # COUNTDOWN TIMER

    @st.fragment(run_every="1s")
    def show_timer():

        elapsed = int(
            time.time() - st.session_state.timer_start
        )

        remaining = max(0, 60 - elapsed)

        if remaining > 0:
            st.info(f"⏱️ Time Remaining: {remaining} seconds")

        else:
            st.session_state.time_up = True
            st.error("⏰ Time Up!")

    show_timer()

    st.divider()

    answer_key = f"answer_{role}_{index}"

    answer = st.text_area(
        "Write your answer here",
        key=answer_key,
        height=150,
        disabled=st.session_state.submitted
    )

    # CHECK ANSWER

    if not st.session_state.submitted:

        if st.button("Check My Answer", type="primary"):

            if not answer.strip():
                st.warning("Please write your answer first.")

            else:
                words = answer.lower().split()

                matched = sum(
                    1 for keyword in keywords
                    if keyword.lower() in answer.lower()
                )

                score = round(
                    (matched / len(keywords)) * 10
                )

                score = min(10, score)

                st.session_state.scores[index] = score
                st.session_state.answers[index] = answer
                st.session_state.submitted = True

                st.rerun()

    # SHOW FEEDBACK

    if st.session_state.submitted:

        score = st.session_state.scores[index]

        st.metric("Your Score", f"{score}/10")

        if score >= 8:
            st.success("Excellent! Very good answer!")

        elif score >= 5:
            st.info("Good effort! Keep improving.")

        else:
            st.warning("Keep practising and improve your answer.")

        st.subheader("📝 Sample Answer")
        st.write(sample)

        st.caption(
            "Scoring is based on keyword matching, "
            "not a real AI evaluation."
        )

        st.divider()

        if index < 9:

            if st.button("Next Question ➡️", type="primary"):

                st.session_state.question_index += 1
                st.session_state.submitted = False
                st.session_state.time_up = False
                st.session_state.timer_start = time.time()

                st.rerun()

        else:

            if st.button("View Final Result 🏆", type="primary"):

                st.session_state.completed = True
                st.rerun()

    st.caption("AI Interview Coach | Interview Practice")

# ---------------- FINAL RESULT ----------------

elif st.session_state.completed:

    st.balloons()

    st.title("🏆 Interview Completed!")

    st.subheader(
        f"Congratulations, {st.session_state.student_name}!"
    )

    st.write(
        f"Role: {st.session_state.role}"
    )

    total_score = sum(st.session_state.scores.values())

    st.metric(
        "Final Score",
        f"{total_score}/100"
    )

    percentage = total_score

    st.progress(percentage / 100)

    st.subheader("📊 Performance Summary")

    st.write(
        f"Questions Attempted: {len(st.session_state.scores)}/10"
    )

    st.write(
        f"Percentage: {percentage}%"
    )

    if percentage >= 80:
        st.success("Excellent Performance! 🌟")

    elif percentage >= 60:
        st.info("Good Performance! Keep practising.")

    elif percentage >= 40:
        st.warning("Average Performance. More practice needed.")

    else:
        st.error("Keep learning and practising!")

    st.subheader("Question-wise Scores")

    for i in range(10):

        score = st.session_state.scores.get(i, 0)

        st.write(
            f"Question {i + 1}: {score}/10"
        )

    st.divider()

    if st.button("Practice Again", type="primary"):

        st.session_state.started = False
        st.session_state.completed = False
        st.session_state.question_index = 0
        st.session_state.scores = {}
        st.session_state.answers = {}
        st.session_state.submitted = False
        st.session_state.time_up = False
        st.session_state.timer_start = None

        st.rerun()

    st.caption("AI Interview Coach | Developed using Python and Streamlit")
