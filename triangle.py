def main():
    n = int(input("What should be the height: "))
    height(n)
def height(n):
    for i in range(n):
        print("*" * (i + 1))
        
if __name__ == "__main__":
    main()