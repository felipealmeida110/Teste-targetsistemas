numero = int(input("Informe um número: "))

a, b = 0, 1

pertence = (numero == 0 or numero == 1)

while b < numero:
    a, b = b, a + b

if b == numero:
    pertence = True

if pertence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")