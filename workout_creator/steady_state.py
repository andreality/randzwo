from random import randint, choice, uniform


def create_steady_state(power, max_duration=10):
    results = dict()
    results["duration"] = str(randint(1, max_duration) * 60)
    has_target_cadence = choice([True, False])
    if has_target_cadence:
        results["target_cadence"] = str(randint(65, 110))
    is_ramp = choice([True, False])
    results["is_ramp"] = is_ramp
    results["has_target_cadence"] = has_target_cadence
    if is_ramp:
        power_differential = uniform(-0.25, 0.25)
        results["power_low"] = str(power - power_differential)
        results["power_high"] = str(power + power_differential)
    return results
