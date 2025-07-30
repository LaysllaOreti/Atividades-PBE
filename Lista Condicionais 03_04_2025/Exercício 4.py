idade = int(input("Digite sua idade: "))
if idade >= 18 and idade < 70:
  print("Seu voto é obrigatório")
elif idade == 16 or idade == 17 or idade > 70:
  print("Seu voto é facultativo")
else:
  print("Você não pode votar")
