def add(a, b):
    # This function adds a to b
    return a + b

def multiply(a, b):
    # This function multiply a*b
    return a * b

def divide(a, b):
    # This function divide a/b only if b is not 0
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    # This function power a with b
    return a ** b