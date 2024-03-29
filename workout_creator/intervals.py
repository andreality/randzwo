from random import randint, uniform, choice

RECOVERY_POWER = 0.5

# 1. Decide whether intervals or steady state
coin_flip = randint(0, 1)
if coin_flip == 0:
    section_type = "IntervalsT"
else:
    section_type = "SteadyState"

total_time = 0


def calculate_time(on_duration, off_duration, num_intervals):
    return (float(on_duration) + float(off_duration)) * float(num_intervals)


def create_return_dict(on_duration, off_duration, num_intervals, off_power=RECOVERY_POWER):
    return {"on_duration": str(on_duration),
            "off_duration": str(off_duration),
            "num_intervals": str(num_intervals),
            "off_power": str(off_power)}


def create_intervals(on_power):
    # decide if regular intervals or over-unders
    is_over_under = False
    if on_power > 1.0 and on_power < 1.2:
        is_over_under = choice([True, False])
    if is_over_under:
        intervals = create_over_unders(on_power)
        return intervals
    if on_power < 0.9:
        intervals = create_tempo_intervals()
    elif on_power < 1.0:
        intervals = create_threshold_intervals()
    elif on_power < 1.15:
        intervals = create_vo2max_intervals()
    else:
        intervals = create_micro_intervals()
    return intervals


def create_over_unders(on_power):
    on_duration = uniform(1, 2) * 60
    off_duration = on_duration * on_power
    off_power = 1 - (on_power - 1)
    num_intervals = randint(2, 5)
    return create_return_dict(on_duration, off_duration, num_intervals, off_power=off_power)


def create_vo2max_intervals():
    on_duration = randint(2, 5) * 60
    off_duration = on_duration
    num_intervals = randint(4, 7)
    return create_return_dict(on_duration, off_duration, num_intervals)


def create_micro_intervals():
    on_duration = randint(1, 3) * 15
    off_duration = on_duration
    num_intervals = randint(6, 12)
    return create_return_dict(on_duration, off_duration, num_intervals)


def create_threshold_intervals():
    on_duration = randint(5, 10) * 60
    off_duration = 0.5 * on_duration
    num_intervals = randint(2, 4)
    return create_return_dict(on_duration, off_duration, num_intervals)


def create_tempo_intervals():
    on_duration = randint(5, 15) * 60
    off_duration = 0.5 * on_duration
    if on_duration < 8:
        num_intervals = randint(2, 6)
    else:
        num_intervals = randint(2, 3)
    return create_return_dict(on_duration, off_duration, num_intervals)

