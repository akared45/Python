
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
op = input("Nhập phép tính")
match op :
    case "+":
        result = a + b
        print(f"Kết quả: {a} + {b} = {result}")
    case "-":
        result = a - b
        print(f"Kết quả: {a} - {b} = {result}")
    case "*":
        result = a * b
        print(f"Kết quả: {a} * {b} = {result}")
    case "/":
        if b == 0:
            print("Lỗi: Không thể chia cho 0!")
        else:
            result = a / b
            print(f"Kết quả: {a} / {b} = {result}")
    case _: 
        print("Lỗi: Phép toán không hợp lệ! Chọn +, -, *, /")
