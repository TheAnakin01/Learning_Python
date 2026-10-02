import random
import sys

def main():
    number = random.randint(0, 100)
    count = 0
    while True:
        try:
            guess = int(input("Whats your guess?: "))
            if guess > number:
                print("Too High")
                count += 1
            elif guess < number:
                print("Too low")
                count += 1
            elif guess == number:
                print("You Got it!")
                count += 1
                print(count)
                sys.exit()
        except ValueError:
            print("Invalid Input")

if __name__ == "__main__":
    main()