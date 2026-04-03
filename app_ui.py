import streamlit as st
import numpy as np
from PIL import Image
import time

from modules.performance_dashboard import calculate_dashboard
from modules.progress_graph import show_progress
from modules.emotion_graph import show_emotion_graph
from modules.emotion_detection import detect_emotion
from modules.ai_teacher import give_learning_content
from modules.ai_explainer import explain_topic
from modules.quiz_generator import generate_quiz
from modules.recommendation import recommend_learning, learning_path
from modules.engagement_prediction import predict_engagement
from modules.study_tracker import calculate_study_time
from modules.focus_engine import calculate_focus_score, get_focus_level

st.title("WELCOME TO DIVE IN STUDIES")

# ---------------- Session Variables ----------------

if "focus_history" not in st.session_state:
    st.session_state["focus_history"] = []

if "emotion_history" not in st.session_state:
    st.session_state["emotion_history"] = []

if "quiz_data" not in st.session_state:
    st.session_state["quiz_data"] = None

if "start_time" not in st.session_state:
    st.session_state["start_time"] = time.time()

if "quiz_start_time" not in st.session_state:
    st.session_state["quiz_start_time"] = None


# ---------------- Emotion Detection ----------------

st.header("Emotion Detection")

camera_image = st.camera_input("Capture your face")

if camera_image is not None:

    image = Image.open(camera_image)
    frame = np.array(image)

    emotion = detect_emotion(frame)

    st.session_state["emotion"] = emotion
    st.session_state["emotion_history"].append(emotion)

    st.success(f"Detected Emotion: {emotion}")

    motivation = give_learning_content(emotion)

    st.write("AI Teacher:", motivation)


# ---------------- Topic Input ----------------

st.header("Learning Topic")

topic = st.text_input("Enter Topic")

if st.button("Explain Topic"):

    if not topic:
        st.warning("Please enter a topic")

    else:
        emotion = st.session_state.get("emotion", "neutral")

        explanation = explain_topic(topic, emotion)

        st.write("AI Explanation:")
        st.write(explanation)


# ---------------- Adaptive Difficulty ----------------

difficulty = "medium"

if st.session_state["focus_history"]:

    last_focus = st.session_state["focus_history"][-1]

    if last_focus < 0.4:
        difficulty = "easy"

    elif last_focus < 0.7:
        difficulty = "medium"

    else:
        difficulty = "hard"


# ---------------- Generate Quiz ----------------

if st.button("Generate Quiz"):

    if not topic:
        st.warning("Please enter a topic first")

    else:

        with st.spinner("Generating quiz..."):

            quiz_text = generate_quiz(topic, difficulty)

        if not quiz_text:
            st.error("Quiz generation failed")

        else:

            st.session_state["quiz_data"] = quiz_text
            st.session_state["quiz_start_time"] = time.time()

            st.success("Quiz Generated Successfully")


# ---------------- Display Quiz ----------------

if st.session_state["quiz_data"]:

    st.header(f"Quiz ({difficulty.capitalize()} Level)")

    quiz_text = st.session_state["quiz_data"]

    questions = quiz_text.split("Question:")

    user_answers = []
    correct_answers = []

    for i, q in enumerate(questions[1:], 1):

        lines = q.strip().split("\n")

        if len(lines) < 5:
            continue

        question = lines[0]

        options = []
        answer = ""

        for line in lines:

            line = line.strip()

            if line.startswith(("A)", "B)", "C)", "D)")):
                options.append(line)

            if line.startswith("Answer"):
                answer = line.split(":")[1].strip()

        if len(options) < 4:
            continue

        correct_answers.append(answer)

        choice = st.radio(
            f"Q{i}: {question}",
            options,
            index=None,
            key=f"q{i}"
        )

        user_answers.append(choice[0] if choice else None)


    # ---------------- Submit Quiz ----------------

    if st.button("Submit Quiz"):

        score = 0

        st.subheader("Quiz Feedback")

        for idx, (u, c) in enumerate(zip(user_answers, correct_answers)):

            if u == c:
                score += 1
                st.markdown(f"✅ Question {idx+1}: Correct")

            else:
                st.markdown(
                    f"❌ Question {idx+1}: Wrong | Correct Answer: **{c}**"
                )

        quiz_accuracy = score / len(correct_answers)

        st.success(f"Quiz Accuracy: {quiz_accuracy*100:.2f}%")

        # ---------------- Response Time ----------------

        response_time = time.time() - st.session_state["quiz_start_time"]

        st.write(f"Response Time: {response_time:.2f} seconds")

        # ---------------- Study Time ----------------

        study_time = calculate_study_time(st.session_state["start_time"])

        st.write(f"Study Time: {study_time:.2f} minutes")

        # ---------------- Emotion ----------------

        emotion = st.session_state.get("emotion", "neutral")

        # ---------------- Focus Engine ----------------

        focus = calculate_focus_score(
            emotion,
            quiz_accuracy,
            response_time,
            study_time
        )

        focus_level = get_focus_level(focus)

        st.success(f"Focus Score: {focus}")
        st.write(f"Focus Level: {focus_level}")

        st.session_state["focus_history"].append(focus)

        # ---------------- Recommendation ----------------

        st.info(recommend_learning(focus))
        st.info(learning_path(topic, focus))

        # ---------------- Graphs (AFTER QUIZ ONLY) ----------------

        st.subheader("Learning Analytics")

        # Progress Graph
        fig1 = show_progress(st.session_state["focus_history"])
        st.pyplot(fig1)

        # Emotion Graph
        fig2 = show_emotion_graph(st.session_state["emotion_history"])
        st.pyplot(fig2)


# ---------------- Engagement Prediction ----------------

if st.button("Predict Engagement Level"):

    prediction = predict_engagement(st.session_state["emotion_history"])

    st.success(f"Predicted Engagement Score: {prediction}/4")

    if prediction > 3:
        st.write("Student engagement improving")

    elif prediction > 2:
        st.write("Student engagement moderate")

    else:
        st.write("Student engagement low")


# ---------------- Student Performance Dashboard ----------------

if st.button("Show Performance Dashboard"):

    avg_focus, best_focus, sessions = calculate_dashboard(
        st.session_state["focus_history"],
        st.session_state["start_time"]
    )

    st.subheader("Student Performance Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Focus Score", avg_focus)
    col2.metric("Best Focus Score", best_focus)
    col3.metric("Sessions Completed", sessions)