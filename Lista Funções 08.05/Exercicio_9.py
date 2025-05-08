def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperaturas_graus_celsius = [30, 100, 0]

temperaturas_graus_fahrenheit = [celsius_para_fahrenheit(temp) for temp in temperaturas_graus_celsius]

for c, f in zip(temperaturas_graus_celsius, temperaturas_graus_fahrenheit):
    print(f"Grau Celsiu {c}°C = Grau Fahrenheit {f:.1f}°F")
