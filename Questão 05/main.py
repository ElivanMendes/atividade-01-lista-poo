list_numbers = []

for i in range(20):
    number = int(input(f'Informe o {i + 1} Numero: '))
    list_numbers.append(number)

numbers_par = list(filter(lambda x: x % 2 == 0, list_numbers))
numbers_impar = list(filter(lambda x: x % 2 != 0, list_numbers))

print(f'\nNumeros: {list_numbers}')
print(f'Numeros Par: {numbers_par}')
print(f'Numeros Impar: {numbers_impar}')
