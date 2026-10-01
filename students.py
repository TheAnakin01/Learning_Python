students = [
    {"name": "Riya", "marks": 82},
    {"name": "Aman", "marks": 67},
    {"name": "Zoya", "marks": 91},
    {"name": "Kabir", "marks": 76},
]

def main():
     good = get_students(students)
     ordered = sorted_students(good)
     for student in ordered:
         print(f"{student["name"]}: {student["marks"]}")

def get_students(students):
    counts = []
    for student in students:
        if student["marks"] > 75:
            counts.append(student)
    return counts

def sorted_students(counts):
    return sorted(counts, key=lambda s: s["marks"])
    
if __name__ == "__main__":
    main()