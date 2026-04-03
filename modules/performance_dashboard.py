def calculate_dashboard(focus_scores, study_time):

    if len(focus_scores) == 0:
        return 0, 0, 0

    avg_focus = sum(focus_scores) / len(focus_scores)

    best_focus = max(focus_scores)

    sessions = len(focus_scores)

    return round(avg_focus,2), best_focus, sessions