def calculate_focus(emotion, quiz_score):

    if emotion == "happy":
        emotion_score = 90
    elif emotion == "neutral":
        emotion_score = 70
    elif emotion == "sad":
        emotion_score = 50
    elif emotion == "angry":
        emotion_score = 40
    else:
        emotion_score = 60

    focus_score = (0.6 * quiz_score) + (0.4 * emotion_score)

    return round(focus_score, 2)