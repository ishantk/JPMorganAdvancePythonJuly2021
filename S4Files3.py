import csv

# Reading the Data
"""
file = open("students.csv", "r")
reader = csv.reader(file)

print(reader, type(reader))

for row in reader:
    print(row)
"""

with open("students.csv", "r") as file:
    # reader = csv.reader(file)
    # print(reader, type(reader))
    # for row in reader:
    #     print(row)

    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# Write the Data
with open("speeds.csv", "w", newline='') as file:
    # writer = csv.writer(file)
    # writer.writerow(["Sn", "vehicle", "speed", "date", "time"])
    # writer.writerow([1, "PB10AB1234", 70, "10th July, 2021", "19:00"])
    # writer.writerow([2, "CH10PQ334", 55, "11th July, 2021", "21:00"])

    # rows = [
    #     ["Sn", "vehicle", "speed", "date", "time"],
    #     [1, "PB10AB1234", 70, "10th July, 2021", "19:00"],
    #     [2, "CH10PQ334", 55, "11th July, 2021", "21:00"]
    # ]
    # writer.writerows(rows)

    field_names = ["Sn", "vehicle", "speed", "date", "time"]
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'Sn': '1', 'vehicle': 'PB10AB1234', 'speed': '80', 'date': '10th July 2021', 'time': '19:00'})

    print("Data Written")


with open("speeds-with-tabs.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter="\t")
    rows = [
        ["Sn", "vehicle", "speed", "date", "time"],
        [1, "PB10AB1234", 70, "10th July, 2021", "19:00"],
        [2, "CH10PQ334", 55, "11th July, 2021", "21:00"]
    ]
    writer.writerows(rows)
    print("Data Written")