list = []

for i in range(4):
    note = float(input(f'Informe a {i + 1} Nota: '))
    list.append(note)

average = sum(list) / len(list)

print(f'\nNotas: {list}\nMédia: {average:.2f}')
