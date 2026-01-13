"""
Faça um programa que receba uma quantidade indefinida
de valores correspondentes a "saldo em conta",
mas quando o usuário apertar "enter" sem digitar valor algum,
o programa para de receber valores, e exibe a soma
de todos os valore digitados anteriormente.
"""
saldo_em_conta = 0
while True:
    entrada = input("Digite o valor do saldo em conta:")
    if entrada == "":
        break
    saldo_em_conta += float(entrada)
print(f"O saldo total em conta é: {saldo_em_conta}")
