# Focus / Engagement Engine for Emotion Adaptive Learning System

# Emotion → numerical engagement score
emotion_score_map = {
    "happy": 0.9,
    "neutral": 0.7,
    "surprise": 0.75,
    "sad": 0.4,
    "angry": 0.3,
    "fear": 0.35,
    "disgust": 0.3
}


def normalize_emotion(emotion):
    """
    Normalize emotion label from emotion detection model
    """
    if not emotion:
        return "neutral"

    emotion = emotion.lower().strip()

    if emotion not in emotion_score_map:
        return "neutral"

    return emotion


def calculate_focus_score(emotion, quiz_accuracy, response_time, study_time):
    """
    Calculate focus score using emotion and learning performance
    """

    emotion = normalize_emotion(emotion)

    emotion_score = emotion_score_map.get(emotion, 0.7)

    response_speed_score = max(0, 1 - (response_time / 10))

    study_time_score = min(study_time / 60, 1)

    focus_score = (
        0.4 * emotion_score +
        0.3 * quiz_accuracy +
        0.2 * response_speed_score +
        0.1 * study_time_score
    )

    return round(focus_score, 2)


def get_focus_level(score):
    """
    Convert focus score to focus level
    """

    if score < 0.4:
        return "Low Focus"

    elif score < 0.7:
        return "Moderate Focus"

    else:
        return "High Focus"