list_average = []

for i in range(10):
    print(f'ALUNO {i + 1}:')

    list_notes = []

    for i in range(4):
        note = float(input(f'Informe a {i + 1} Nota: '))
        list_notes.append(note)

    list_average.append(round(sum(list_notes) / len(list_notes), 2))

list_average = list(filter(lambda x: x >= 7.0, list_average))

print(f'\nMedias Maior que 7.0: {len(list_average)}\nMedias: {list_average}')
