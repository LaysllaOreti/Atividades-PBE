def palavra_palindromo(frase):
    frase = ''.join(c for c in frase.lower() if c.isalnum())
    return frase == frase[::-1]

titulos = ["Ana Ana", "1DSTB-SENAI", "Subi no Onibus"]

for titulo in titulos:
    if palavra_palindromo(titulo):
        print(f'"{titulo}" é um palíndromo.')
    else:
        print(f'"{titulo}" não é um palíndromo.')
