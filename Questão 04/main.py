list_characters = []

for i in range(10):
    character = input(f'Informe o {i + 1} Caracter: ')
    list_characters.append(character)

list_characters = list(filter(lambda x: x != 'a' and x != 'e'
                                        and x != 'i' and x != 'o'
                                        and x != 'u' and x != 'A'
                                        and x != 'E' and x != 'I'
                                        and x != 'O' and x != 'U', list_characters))

print(f'\nQuantidade de Consoantes: {len(list_characters)}\nConsoantes: {list_characters}')
