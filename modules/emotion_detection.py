import random

def detect_emotion(frame=None):

    emotions = ["happy", "neutral", "sad", "angry"]

    emotion = random.choice(emotions)

    return emotion