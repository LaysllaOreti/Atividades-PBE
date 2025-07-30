dia = int(input("Digite o dia, por favor: "))
mes = int(input("Digite o mês, por favor: "))
ano = int(input("Digite o ano, por favor: "))

if mes < 1 or mes > 12:
    print("A data digitada é inválida, pois o mês deve estar entre 1 e 12.")
else:
    # Mês de fevereiro
    if mes == 2:
        # Verificação ano bissexto:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            # Caso o ano seja bissexto:
            if dia < 1 or dia > 29:
                print("A data digitada está inválida!")
            else:
                print(
                    f"A data no formato dd/mm/aaaa é {dia}/{mes}/{ano}.\nA data de hoje no formato aaaa/mm/dd é {ano}/{mes}/{dia}.")   
        # Caso o ano não seja bissexto:
        else:
            if dia < 1 or dia > 28:
                print("A data digitada está inválida!")
            else:
                print(
                    f"A data no formato dd/mm/aaaa é {dia}/{mes}/{ano}.\nA data de hoje no formato aaaa/mm/dd é {ano}/{mes}/{dia}.")
    # Meses com 31 dias:
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia < 1 or dia > 31:
            print("A data digitada é inválida!")
        else:
            print(
                f"A data no formato dd/mm/aaaa é {dia}/{mes}/{ano}.\nA data de hoje no formato aaaa/mm/dd é {ano}/{mes}/{dia}.")
    # Meses com 30 dias:
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia < 1 or dia > 30:
            print("A data digitada é inválida!")
        else:
            print(
                f"A data no formato dd/mm/aaaa é {dia}/{mes}/{ano}.\nA data de hoje no formato aaaa/mm/dd é {ano}/{mes}/{dia}.")
