def main():
    while True:
        try:
            fraction = input("Whats the fraction: ")
            num, dem = fraction.split("/")
            num = int(num)
            dem = int(dem)
            if num > dem:
                print("Invalid Input")
            elif dem == 0:
                print("Invalid Input")
            else:
                answer = round((num/dem) * 100)
                print(f"Your percentage is {answer}%")
                break 
        except(ValueError):
            print("Invalid Input")


if __name__ == "__main__":
    main()