"""
Faça um progrma que receba 4 alturas usando um laço de repetição e relize
a soma dessas alturas.
"""
soma = 0 # valor final
count = 1 # entradas
while count <= 4:
    altura = float(input(f"Digite a altura {count}: "))
    soma += altura
    count += 1
print(f"A soma das alturas é: {soma}")
