import re

cpf = input("Insira o seu CPF, por favor: ")
padrao = r"\d{3}\.\d{3}\.\d{3}\-\d{2}"
valido = re.match(padrao, cpf)

if valido:
    penultimo_digito = ((int(cpf[0]) * 10) + (int(cpf[1]) * 9) + (int(cpf[2]) * 8) + (int(cpf[4]) * 7) + (int(cpf[5]) * 6) + (int(cpf[6]) * 5) + (int(cpf[8]) * 4) + (int(cpf[9]) * 3) + (int(cpf[10]) * 2)) % 11
    ultimo_digito = ((int(cpf[0]) * 11) + (int(cpf[1]) * 10) + (int(cpf[2]) * 9) + (int(cpf[4]) * 8) + (int(cpf[5]) * 7) + (int(cpf[6]) * 6) + (int(cpf[8]) * 5) + (int(cpf[9]) * 4) + (int(cpf[10]) * 3) + (int(cpf[12]) * 2)) % 11

    if penultimo_digito >= 2:
        digito1 = 11 - penultimo_digito
    else:
        digito1 = 0
    if ultimo_digito >= 2:
        digito2 = 11 - ultimo_digito
    else:
        digito2 = 0

    if int(cpf[12]) == digito1 and int(cpf[13]) == digito2:
        print("O CPF digitado é válido!")
    else:
        print("O CPF digitado é inválido!")
else:
    print("O CPF inserido não foi digitado corretamente!")
