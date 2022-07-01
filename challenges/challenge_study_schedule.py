def study_schedule(permanence_period, target_time):
    acc = 0
    try:
        for init, final in permanence_period:
            if init <= target_time <= final:
                acc += 1
        return acc
    except TypeError:
        return None