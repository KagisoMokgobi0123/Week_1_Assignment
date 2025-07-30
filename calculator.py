num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
operator = input("Input operator(+,-,/,*): ")

def calculation():
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = float(num1) * float(num2)
    elif operator == "/":
        answer = float(num1)/float(num2)
    return answer

if __name__ == "__main__":
    print(f"{num1} {operator} {num2} = {calculation()}")