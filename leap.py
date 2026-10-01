def main():
    year = int(input("Year: "))
    if is_leap(year):
        print("Year is a leap year")
    else:
        print("Year is not a leap year")

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    main()