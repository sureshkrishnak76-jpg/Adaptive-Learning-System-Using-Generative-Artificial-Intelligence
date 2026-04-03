import matplotlib.pyplot as plt

def show_emotion_graph(emotions):

    emotion_map = {
        "angry": 1,
        "sad": 2,
        "neutral": 3,
        "happy": 4
    }

    values = [emotion_map.get(e, 3) for e in emotions]

    sessions = list(range(1, len(values) + 1))

    fig, ax = plt.subplots()

    ax.plot(sessions, values, marker='o')

    ax.set_title("Emotion Trend During Learning")
    ax.set_xlabel("Session")
    ax.set_ylabel("Emotion Level")

    ax.set_yticks([1,2,3,4])
    ax.set_yticklabels(["Angry","Sad","Neutral","Happy"])

    ax.grid(True)

    return fig