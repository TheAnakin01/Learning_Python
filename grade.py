def main():
    marks = int(input("Marks: "))
    grade = get_grade(marks)
    print(f"Grades are {grade}")

def get_grade(marks):
    if marks > 100 or marks < 0:
        return("Invalid")
    elif marks >= 90:
        return("A")
    elif marks >= 80:
        return("B")
    elif marks >= 70:
        return("C")
    elif marks >= 60:
        return("D")
    elif marks >= 0:
        return("F")

if __name__ == "__main__":
    main()