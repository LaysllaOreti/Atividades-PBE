from datetime import datetime

data_input = input("Digite uma data no formato dd/mm/aaaa: ")

data_formatada = datetime.strptime(data_input, "%d/%m/%Y").strftime("%Y-%m-%d")

print("A data formatada é:", data_formatada)
