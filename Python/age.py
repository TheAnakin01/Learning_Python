name = input("What is your name? ")
age = input("Age: ")

def find_age(age):
    new_age = int(age) + 5
    return new_age

print(f"In 5 years, {name} will be {new_age} years old.")