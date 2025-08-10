lista_cidades = [
    "são paulo", "campinas", "guarulhos", "são bernardo do campo", 
    "santo andré", "osasco", "ribeirão preto", "sorocaba", "santos", 
    "são josé dos campos", "bauru", "piracicaba", "taubaté", 
    "itaquaquecetuba", "são josé do rio preto", "franca", 
    "presidente prudente", "araçatuba", "araraquara", "marília", 
    "jundiaí", "americana"
]

lista_escolhas = ['1', '2', '3', '4']

grafo_original = {
    "são paulo": [
        ("guarulhos", 20),
        ("osasco", 16),
        ("santo andré", 18),
        ("são bernardo do campo", 22),
        ("campinas", 93)
    ],
    "campinas": [
        ("são paulo", 93),
        ("jundiaí", 42),
        ("piracicaba", 63),
        ("americana", 22),
        ("sorocaba", 120)
    ],
    "guarulhos": [
        ("são paulo", 20),
        ("são josé dos campos", 80),
        ("itaquaquecetuba", 15)
    ],
    "são bernardo do campo": [
        ("são paulo", 22),
        ("santo andré", 10),
        ("santos", 58)
    ],
    "santo andré": [
        ("são paulo", 18),
        ("são bernardo do campo", 10),
        ("osasco", 25)  
    ],
    "osasco": [
        ("são paulo", 16),
        ("guarulhos", 28)  
    ],
    "ribeirão preto": [
        ("franca", 100),
        ("araraquara", 110),
        ("são josé do rio preto", 210)
    ],
    "sorocaba": [
        ("campinas", 120),
        ("itaquaquecetuba", 140),
        ("bauru", 230)
    ],
    "santos": [
        ("são bernardo do campo", 58),
        ("guarulhos", 85)  
    ],
    "são josé dos campos": [
        ("guarulhos", 80),
        ("taubaté", 40),
        ("americana", 170)  
    ],
    "bauru": [
        ("sorocaba", 230),
        ("marília", 90),
        ("araçatuba", 170)
    ],
    "piracicaba": [
        ("campinas", 63),
        ("sorocaba", 75),   
        ("jundiaí", 90)     
    ],
    "taubaté": [
        ("são josé dos campos", 40),
        ("guarulhos", 125)  
    ],
    "itaquaquecetuba": [
        ("guarulhos", 15),
        ("sorocaba", 140),
        ("santo andré", 25) 
    ],
    "são josé do rio preto": [
        ("ribeirão preto", 210),
        ("araçatuba", 180),
        ("araraquara", 160)
    ],
    "franca": [
        ("ribeirão preto", 100),
        ("araraquara", 120)
    ],
    "presidente prudente": [
        ("araçatuba", 240),
        ("marília", 150)
    ],
    "araçatuba": [
        ("bauru", 170),
        ("são josé do rio preto", 180),
        ("presidente prudente", 240)
    ],
    "araraquara": [
        ("ribeirão preto", 110),
        ("franca", 120),
        ("são josé do rio preto", 160)
    ],
    "marília": [
        ("bauru", 90),
        ("presidente prudente", 150)
    ],
    "jundiaí": [
        ("campinas", 42),
        ("são paulo", 60)
    ],
    "americana": [
        ("campinas", 22),
        ("piracicaba", 40)
    ]
}


def tela_inicial():
    print("Bem vindo ao nosso aplicativo de GPS!")
    print('O nosso GPS possui 22 cidades mapeadas dentro do estado de São Paulo.')
    while True:
        print('\nTemos as seguintes funcionalidades:\n1 - Consultar cidades mapeadas;\n2 - Visualizar/alterar distâncias entre as cidades;\n3 - Usar o GPS;\n4 - Sair.')
        escolha = input('Para selecionar a funcionalidade desejada, digite o número correspondende. Qual a sua escolha?\n')
        if escolha in lista_escolhas:
            if escolha == '1':
                print('Seguem as cidades mapeadas:\n')

                for cidade in lista_cidades:
                    print(f'- {cidade}')

                print('\nVoltando para a tela inicial.\n')
            
            elif escolha == '2':
                atualizar_pesos()

            elif escolha == '3':
                break

            elif escolha == '4':
                print('Encerrando o programa.')
                exit()

        else:
            print('Opção inválida, tente novamente\n')
            continue


def atualizar_pesos():
    print("\nVisualização e edição de distâncias entre cidades")    
    print("\nSelecione uma cidade para editar suas conexões:")

    for i, cidade in enumerate(lista_cidades, 1):
        print(f"{i} - {cidade}")

    try:
        opcao = int(input("\nDigite o número da cidade (0 para voltar): "))
        if opcao == 0: 
            return
        cidade_origem = lista_cidades[opcao-1]
    except (ValueError, IndexError):
        print("Seleção inválida!")
        return

    conexoes = grafo_original.get(cidade_origem, [])
    print(f"\nConexões de {cidade_origem}:")
    
    if not conexoes:
        print("Nenhuma conexão definida")
        return
    
    for i, (vizinho, peso) in enumerate(conexoes, 1):
        print(f"{i} - {vizinho}: {peso} km")

    try:
        idx = int(input("\nDigite o número da conexão para editar (0 para cancelar): ")) - 1
        if idx == -1:
            return
            
        cidade_dest, peso_antigo = conexoes[idx]
        novo_peso = int(input(f"Novo peso para {cidade_origem} → {cidade_dest}: "))

        conexoes[idx] = (cidade_dest, novo_peso)
        
        for i, (viz, peso) in enumerate(grafo_original[cidade_dest]):
            if viz == cidade_origem:
                grafo_original[cidade_dest][i] = (cidade_origem, novo_peso)
                break
        
        print("\nConexão atualizada com sucesso!")
    
    except (ValueError, IndexError):
        print("Operação inválida!")


def pontos_gps():
    print(f'Agora precisamos saber quais são as cidades de inicio e destino.\n')
    while True:
        ponto_partida = input('Em qual cidade você está?\n').strip().lower()

        if ponto_partida in lista_cidades:
            ponto_destino = input('Qual é a cidade de destino?\n').strip().lower()

            if ponto_destino in lista_cidades:

                if ponto_destino != ponto_partida:
                    print(f'Certo!')
                    return ponto_partida, ponto_destino
                
                else:
                    print(f'O ponto destino não pode ser igual ao inicial, tente novamente')
                    continue

            else:
                print(f'O ponto destino não é valido, tente novamente')
                continue

        else:
            print(f'O ponto de partida não é válido, tente novamente')
            continue


def algoritmo_prim(grafo, inicio):
    visitados = set()
    agm = []  
    arestas_candidatas = []

    visitados.add(inicio)
    for vizinho, peso in grafo[inicio]:
        arestas_candidatas.append((peso, inicio, vizinho))

    while arestas_candidatas:
        arestas_candidatas.sort()
        peso, u, v = arestas_candidatas.pop(0)

        if v not in visitados:
            visitados.add(v)
            agm.append((u, v, peso))
            
            for vizinho, w in grafo[v]:
                if vizinho not in visitados:
                    arestas_candidatas.append((w, v, vizinho))

    return agm


def algoritmo_dijkstra(grafo, inicio):
    distancias = {vertice: float('inf') for vertice in grafo}
    anteriores = {vertice: None for vertice in grafo}  
    distancias[inicio] = 0
    visitados = set()
    
    while len(visitados) < len(grafo):
        vertice_minimo = None
        distancia_minima = float('inf')
        
        for vertice in grafo:
            if vertice not in visitados and distancias[vertice] < distancia_minima:
                distancia_minima = distancias[vertice]
                vertice_minimo = vertice
        
        if vertice_minimo is None:
            break
        
        visitados.add(vertice_minimo)
        
        for vizinho, peso in grafo[vertice_minimo]:
            if vizinho not in visitados:
                nova_distancia = distancias[vertice_minimo] + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    anteriores[vizinho] = vertice_minimo  
    
    return distancias, anteriores


def reconstruir_caminho(anteriores, destino):
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]
    return caminho[::-1] 


def criar_grafo_prim(grafo_original, ponto_partida):
    arestas_da_agm = algoritmo_prim(grafo_original, ponto_partida)
    grafo_da_agm = {}
    
    for u, v, peso in arestas_da_agm:
        grafo_da_agm.setdefault(u, []).append((v, peso))
        grafo_da_agm.setdefault(v, []).append((u, peso))

    return grafo_da_agm


def aplicar_dijkstra(grafo_da_agm, ponto_partida):
    distancias_na_agm = algoritmo_dijkstra(grafo_da_agm, ponto_partida)

    return distancias_na_agm


def apresentar_resultado(distancias, anteriores, partida, destino):
    distancia_total = distancias.get(destino, float('inf'))
    if distancia_total == float('inf'):
        print(f"Não há caminho entre {partida} e {destino}")
    else:
        caminho = reconstruir_caminho(anteriores, destino)
        print(f"Distância: {distancia_total} km")
        print("Caminho:", " → ".join(caminho))


def voltar_inicio():
    while True:
        encerrar = input('Deseja realizar uma nova operação(s/n)?\n').lower().strip()

        if encerrar == 's':
            main()
            break
        elif encerrar == 'n':
            print('Encerrando o programa.')
            exit()
        else:
           print('Opção inválida! tente novamente')


def main():
    tela_inicial()
    ponto_partida, ponto_destino = pontos_gps()
    grafo_da_agm = criar_grafo_prim(grafo_original, ponto_partida) 
    distancias, anteriores = aplicar_dijkstra(grafo_da_agm, ponto_partida) 
    apresentar_resultado(distancias, anteriores, ponto_partida, ponto_destino) 
    voltar_inicio()


if __name__ == '__main__':
    main()