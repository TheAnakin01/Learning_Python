def main():
    while True:
        try:
            name = input("Name: ")
            with open("names.txt", 'a') as file:
                file.write( name + "\n")
        except EOFError:
            break

    names = []
    with open("names.txt") as file:
        for line in file:
            names.append(line.rstrip("\n"))

        for name in sorted(names):
            print(name) 


if __name__ == "__main__":
    main()