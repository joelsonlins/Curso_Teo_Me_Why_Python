# Quais numeros são divisiveis por 4 ?

i = 4
while i <= 100:
    resto = i % 4
    if resto == 0:
        print(i)

    i += 1