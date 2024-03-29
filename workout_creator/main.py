from generate_file import generate_zwo_file

for minutes in range(30, 120):
    for _ in range(5):
        generate_zwo_file(minutes)
