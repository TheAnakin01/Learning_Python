import re

phone = input("Input: ")
if re.search(r"^(\+91 )?[6-9]\d{9}$", phone):
    print("Valid")
else:
    print("Invalid")
