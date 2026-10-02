def main():
    while True:
     try:
       number = int(input("Whats the number: "))
       print(f"Your number is {number}")
       break
     except ValueError, EOFError:
       print("Invalid Input") 

if __name__ == "__main__":
    main()