import sys

def add(a, b):
    return a + b

if name == "main":

    if len(sys.argv) != 3:
        print("Usage: python add.py <num1> <num2>")
        sys.exit(1)

    x = int(sys.argv[1])
    y = int(sys.argv[2])
    
    print("Sum:", add(x, y))
