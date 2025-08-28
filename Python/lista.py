import os


restaurantes = [{'Nome':'Savioli', 'Categoria': 'Comida', 'Ativo': True}, {'Nome': 'Gorduchos', 'Categoria': 'Lanche', 'Ativo': False}]

def abertura():
        print('Sabor Express')

def opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair')

def voltar_ao_menu():
    input('\nDigite qualquer tecla para voltar ao menu\n')
    os.system('cls')
    main()

def subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(f'* {texto} *')
    print(linha)
    print()

def escolher():
    escolha = input('Qual será a opção?\n')

    if escolha == '1':
        cadastro_restaurante()
    elif escolha == '2':
        listar_restaurantes()
    elif escolha == '3':
        alterar_status()
    elif escolha == '4':
        encerrar_programa()

def cadastro_restaurante():
    subtitulo('Cadastro de restaurantes')
    nov_res = input('qual será o nome do novo restaurante?\n')
    categoria = input(f'qual é a categoria do restaurante {nov_res}?\n')
    dados_do_restaurante = {'Nome':nov_res, 'Categoria': categoria, 'Ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nov_res} foi adicionado com sucesso!')
    voltar_ao_menu()

def listar_restaurantes():
    subtitulo('Listagem de restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | Status')
    for restaurante in restaurantes:
        nome = restaurante['Nome']
        categoria = restaurante['Categoria']
        ativo = 'Ativado' if restaurante['Ativo'] else 'Desativado'
        print(f'-{nome.ljust(20)} | {categoria.ljust(20)} | {ativo}') 
    voltar_ao_menu()

def alterar_status():
    subtitulo('Alterando o status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que oo status será alterado:\n')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['Ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu()

def encerrar_programa():
    subtitulo('Finalizando o app')
    exit()
    

def main():
    abertura()
    opcoes()
    escolher()

if __name__ == '__main__':
    main()

    

