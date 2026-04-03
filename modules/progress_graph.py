import matplotlib.pyplot as plt

def moving_average(data, window=3):

    smoothed = []

    for i in range(len(data)):

        start = max(0, i - window + 1)

        subset = data[start:i+1]

        smoothed.append(sum(subset) / len(subset))

    return smoothed


def show_progress(scores):

    sessions = list(range(1, len(scores) + 1))

    smoothed_scores = moving_average(scores)

    fig, ax = plt.subplots()

    ax.plot(sessions, scores, marker='o', label="Raw Focus Score")

    ax.plot(sessions, smoothed_scores, linestyle='--', label="Learning Trend")

    ax.set_title("Student Learning Progress")

    ax.set_xlabel("Session")

    ax.set_ylabel("Focus Score")

    ax.legend()

    ax.grid(True)

    return fig