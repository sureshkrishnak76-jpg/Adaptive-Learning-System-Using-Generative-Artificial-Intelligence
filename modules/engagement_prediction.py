def predict_engagement(emotions):

    emotion_map = {
        "angry":1,
        "sad":2,
        "neutral":3,
        "happy":4
    }

    values = [emotion_map.get(e,3) for e in emotions]

    if len(values) == 0:
        return 0

    prediction = sum(values) / len(values)

    return round(prediction,2)