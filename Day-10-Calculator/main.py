from logo import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)
    function = input("Choose wisely: ")

    num2 = float(input("What's the second number? "))

    answer = operations[function](num1, num2)

    print(f"{num1} {function} {num2} = {answer}")

    done = input("Are you done yet? (y/n)")

    while done == "n":
        print(f"Last answer is {answer}")
        for symbol in operations:
            print(symbol)
        function = input("Choose wisely: ")
        num3 = float(input("What's next number? "))
        num1 = answer
        answer = operations[function](num1, num3)
        print(f"{num1} {function} {num3} = {answer}")
        done = input("Are you done yet? (y/n) ")
    if done == "y":
        clear() # comment it if you're on PyCharm
        print(logo)
        calculator()

print(logo)
calculator()
