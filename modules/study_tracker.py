import time

def calculate_study_time(start_time):

    duration = (time.time() - start_time) / 60

    return round(duration,2)