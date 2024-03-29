import xml.etree.ElementTree as ET
from random import uniform, randint
from intervals import create_intervals, calculate_time
from steady_state import create_steady_state


def generate_zwo_file(target_minutes):
    target_time = target_minutes * 60

    root = ET.Element("workout_file")

    author = ET.SubElement(root, "author")
    author.text = "Andrea Sweny"

    name = ET.SubElement(root, "name")

    desc = ET.SubElement(root, "description")
    desc.text = "A randomly generated workout."

    sport_type = ET.SubElement(root, "sportType")
    sport_type.text = "bike"

    tags = ET.SubElement(root, "tags")
    workout = ET.SubElement(root, "workout")

    total_time = 0
    warmup_duration = randint(5, 10) * 60
    warmup = ET.SubElement(workout, "Warmup", Duration=str(warmup_duration), PowerLow="0.4", PowerHigh="0.85")
    total_time += warmup_duration

    while total_time < target_time:
        on_power = round(uniform(0.5, 1.5), 2)
        if on_power < 0.8:  # steady state
            results = create_steady_state(power=on_power, max_duration=10)
            duration = int(results["duration"])
            if results["is_ramp"]:
                item = ET.SubElement(workout,
                                     "Ramp",
                                     Duration=results["duration"],
                                     PowerHigh=results["power_high"],
                                     PowerLow=results["power_low"])
            else:
                item = ET.SubElement(workout,
                                     "SteadyState",
                                     Power=str(on_power),
                                     Duration=results["duration"])
                if results["has_target_cadence"]:
                    item.set("Cadence", results["target_cadence"])
        else:
            intervals = create_intervals(on_power)
            item = ET.SubElement(workout,
                                 "IntervalsT",
                                 Repeat=intervals["num_intervals"],
                                 OnDuration=intervals["on_duration"],
                                 OffDuration=intervals["off_duration"],
                                 OnPower=str(on_power),
                                 OffPower=intervals["off_power"])
            duration = calculate_time(on_duration=intervals["on_duration"],
                                      off_duration=intervals["off_duration"],
                                      num_intervals=intervals["num_intervals"])
        # print(item.OnPower)
        total_time += duration
        item = ET.SubElement(workout, "SteadyState", Power=f"0.55", Duration="60")
    print_time = round(total_time / 60)
    print(f"Total workout time is {print_time}.")
    cooldown = ET.SubElement(workout, "Cooldown", PowerLow="0.75", PowerHigh="0.55", Duration="300")

    name.text = f"Random Workout {print_time}"
    tree = ET.ElementTree(root)

    tree.write(f'/Users/andreasweny/Documents/Zwift/workouts/71007/random_workout_{print_time}.zwo')



