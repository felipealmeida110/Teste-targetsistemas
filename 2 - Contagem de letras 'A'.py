nome = input("Informe uma string: ")

quant_a = nome.lower().count('a')

if quant_a:
    print(f"Tem {quant_a} Letras A na palavra {nome}")
else:
    print(f"Nenhuma letra A na palavra {nome}")