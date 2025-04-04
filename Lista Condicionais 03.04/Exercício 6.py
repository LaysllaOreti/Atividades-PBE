nota = int(input("Insira uma nota de 0 a 10: "))
if nota == 9 or nota == 10:
  print("Nota A")
elif nota == 7 or nota == 8:
  print("Nota B")
elif nota == 5 or nota == 6:
  print("Nota C")
elif nota == 3 or nota == 4:
  print("Nota D")
elif nota == 2 or nota == 1 or nota == 0:
  print("Nota E")
else:
  print("Nota inválida")
