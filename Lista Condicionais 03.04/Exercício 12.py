n1 = float(input("Insira um número: "))
n2 = float(input("Insira o segundo número: "))
n3 = float(input("Insira o terceiro número: "))

if(n1>n2 and n2>n3):
    print("Ordem decrescente")
elif (n1<n2 and n2<n3):
    print("Ordem crescente")
else:
    print("Números iguais")
