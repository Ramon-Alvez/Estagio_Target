import os
os.system("cls")

print("Comparação de um número existente (ou não) na sequência de fibonacci")

n = int(input("\nDigite o numero que deseja realizar a comparação: "))

num_1 = 0
num_2 = 1
fibonacci = 0

while fibonacci != n: 
    fibonacci = num_1 + num_2   # Cálculo da sequência de fibonacci
    num_1 = num_2               # Aqui precisei inverter a sequência dos números para que a sequência continue rodando automaticamente
    num_2 = fibonacci
    if fibonacci == n:
        print(f"\nO numero informado pertence a sequência.")
        break
    elif fibonacci > n:
        print(f"\nO numero informado não pertence a sequência.")
        break