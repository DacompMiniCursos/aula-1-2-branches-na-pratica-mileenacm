numero = int(input("Digite o número: "))

def tabuada():
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero*i}")
        i += 1
    return

tabuada()

print()

def tabuada_feature(): 
    for i in range(1,11): #ou range(10)
        print(f" {numero} x {i} = {numero*i}")
    return

tabuada_feature()