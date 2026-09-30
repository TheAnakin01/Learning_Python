def main():
    c = float(input("Celcius: "))
    print(celcius_to_f(c))

def celcius_to_f(c):
    fahrenheit = c * 1.8 + 32
    return round(fahrenheit, 1)

if __name__ == "__main__":
    main()