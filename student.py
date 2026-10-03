import csv
def main():
    printer = []
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            printer.append(row)
    sorted_names  = sorted(printer, key=lambda s: s["name"])
    for names in sorted_names:
        print(f"{names['name']} is in {names['house']}")

    with open("output.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "house", "name_length"])
        writer.writeheader()

        for student in sorted_names:
            student["name_length"] = len(student["name"])
            writer.writerow(student)

if __name__ == "__main__":
    main()