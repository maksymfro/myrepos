import art
print(art.logo)

condition = True
while condition:

    operator = input("Choose an operator '+, -, *, /':\n ")
    num1 = int(input("input first number:\n"))
    num2 = int(input("input second number:\n"))

    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        print(num1//num2)

    else:
        print("no such operator")

    continue_deb = input("Type 'y' if you want to continue otherwise type 'n':\n ")
    if continue_deb == "n":
        condition = False

