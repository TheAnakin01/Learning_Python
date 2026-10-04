import sys
from datetime import date

def main():
    text = input("BirthDate: ")
    try: 
        birth = date.fromisoformat(text)
    except ValueError:
        sys.exit("Invalid Input")

    today = date.today()
    diff = today - birth                       
    print(diff.days) 

if __name__ == "__main__":
    main()