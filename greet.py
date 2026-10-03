import sys 

if len(sys.argv) < 2:
    sys.exit("Too few agruments")
elif len(sys.argv) >= 3:
    sys.exit("Too many arguments")
else:
    print(f"hello, {sys.argv[1]}")
