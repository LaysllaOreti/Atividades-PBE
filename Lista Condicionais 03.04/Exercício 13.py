temperatura = float(input("Insira a temperatura atual em graus Celsius: "))
if temperatura < 10:
  print("Frio!")
elif temperatura == 10 or temperatura <=25:
  print("Aconchegante!")
elif temperatura > 25 or temperatura <= 40:
  print("Quente!")
else:
  print("Muito quente!")
