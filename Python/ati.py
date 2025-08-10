lista_soma = ['soma', '1']
lista_sub = ['subtracao', 'subtração', '2']
lista_mult = ['multiplicao', 'multiplicação','3']
lista_div = ['divisão','divisao','4']
lista_geral = lista_soma + lista_sub + lista_mult + lista_div

def intro():
     print('calculadora\ntemos as operações 1 - soma, 2 - subtração, 3 - multiplicação ou 4 - divisão.')

def opcao():
     while True:
          escolha = input('qual operação vc quer?\n').lower()
          if escolha in lista_geral:                
               print('Certo! Agora preciso saber quais serão os números da operação.\n')
               return escolha
          print('opção invalida, tente novamente')

def nums():
     while True:    
          try:
               num1 = float(input('qual seria o primeiro número? \n'))
               num2 = float(input('e o segundo?\n'))  
               return num1, num2
          except ValueError:
               print('valor digitado inválido, tente novamente')

def operacoes(escolha, num1, num2):
     if escolha in lista_soma:
          return num1 + num2
     elif escolha in lista_sub:
          return num1 - num2
     elif escolha in lista_mult:
          return num1 * num2
     elif escolha in lista_div:
          return num1 / num2

def resultado(res):
     print(f'o resultado para a sua conta é {res}')

def main():
     intro()
     operacao = opcao()
     num1, num2 = nums()
     res = operacoes(operacao, num1, num2)
     resultado(res)

if __name__ == '__main__':
     main()
      