import re

url = input("URL: ")

match = re.search(r'^https\:\/\/github\.com\/([a-zA-Z0-9_]+)$', url)
if match:
    print(f"{match.group(1)}")
else:
    print("Invalid")