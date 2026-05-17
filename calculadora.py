def calculadora():

    a = int(input("indique o dígito 1: "))
    b = int(input("indique o dígito 2: "))
    op = input("Indique a operação (+, -, /, *, **) : ")

    if op == "+":
        print(f" Sua adição é {a+b}")
    
    elif op == "-":
        print(f" Sua subtração é {a-b}")

    elif op == "*":
        print(f" Sua multiplicação é {a*b}")
    
    elif op == "/":
        print(f" Sua divisão é {a/b}")
    
    elif op == "**":
        print(f" O valor da exponenciação é {a**b}")
    return 

calculadora()