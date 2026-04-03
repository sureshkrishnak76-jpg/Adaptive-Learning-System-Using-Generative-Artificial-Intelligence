def recommend_learning(focus):

    if focus < 50:
        return "📘 Recommendation: Review the basic concepts again."

    elif focus < 75:
        return "📝 Recommendation: Practice more questions."

    else:
        return "🚀 Recommendation: Move to advanced topics."


def learning_path(topic, focus):

    if focus < 50:
        return f"📚 Learning Path: Review fundamentals of {topic}"

    elif focus < 75:
        return f"📝 Learning Path: Practice exercises on {topic}"

    else:
        return f"🚀 Learning Path: Study advanced concepts related to {topic}"