from modules.emotion_detection import detect_emotion
from modules.ai_teacher import give_learning_content
from modules.ai_explainer import explain_topic
from modules.quiz_generator import generate_quiz
from modules.focus_score import calculate_focus
from modules.progress_graph import show_progress


emotion = detect_emotion()
focus_history = []
content = give_learning_content(emotion)

print("Detected Emotion:", emotion)
print("AI Teacher:", content)


topic = input("\nWhat topic are you studying today? ")


explanation = explain_topic(topic, emotion)

print("\nAI Explanation:")
print(explanation)


quiz = generate_quiz(topic)

print("\nQuiz Time!")
print(quiz)