def calculator():    
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    op = input("Enter the calculation")
    match op :
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
                print("Error: Cannot divide by 0!")
            else:
                result = a / b
                print(f"Result: {a} / {b} = {result}")
        case _:
            print("Error: Invalid calculation rate! Select +, -, *, /")
if __name__ == '__main__':
    calculator()
