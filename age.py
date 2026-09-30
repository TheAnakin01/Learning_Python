def main():
    name = input("What is your name? ")
    age = input("Age: ")
    result = future_age(age, 5)
    print(f"In 5 years, {name} will be {result} years old.")

def future_age(age, years):
    new_age = int(age) + int(years)
    return new_age

if __name__ == "__main__":
    main()
