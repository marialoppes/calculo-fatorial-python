import math

# Converte o valor digitado de string para inteiro para permitir o cálculo do fatorial
numero_inteiro = int(input("Digite um número inteiro entre 1 e 10: "))

# Calcula o fatorial do número informado
fatorial_numero = math.factorial(numero_inteiro)

# Exibe o resultado no terminal
print(f"O fatorial de {numero_inteiro} é {fatorial_numero}.")