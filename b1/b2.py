def calculate():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    op = input("Enter an operator (+, -, *, /): ")

    match op:
        case "+":
            result = a + b
            print(f"Result: {a} + {b} = {result}")
        case "-":
            result = a - b
            print(f"Result: {a} - {b} = {result}")
        case "*":
            result = a * b
            print(f"Result: {a} * {b} = {result}")
        case "/":
            if b == 0:
                print("Error: Cannot divide by zero!")
            else:
                result = a / b
                print(f"Result: {a} / {b} = {result}")
        case _:
            print("Error: Invalid operator! Please choose +, -, *, or /.")

if __name__ == "__main__":
    calculate()
