peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
  print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 25.0:
  print("Seu peso está normal.") 
elif imc >= 25 and imc < 30:
  print("Você está com sobrepeso.") 
elif imc >= 30 and imc < 35:
  print("Você está com obesidade.") 
else:
  print("Você está com obesidade mórbida.")
