pessoas = [{'nome':'luis', 'idade':20, 'cidade':'itu'}, 
           {'nome':'ana', 'idade':37, 'cidade':'salto'}]

nome = input('qual eh o nome a ser alterado ')
idade = int(input('nova idade '))


for pessoa in pessoas:
    if nome == pessoa['nome']:
        pessoa['idade'] = idade
        print('sucesso')

    else:
        print('erro')

print(pessoas)