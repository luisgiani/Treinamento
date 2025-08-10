import heapq

def obter_grafo():
    grafo, mapa_id_para_nome, mapa_nome_para_id = {}, [], {}
    print("--- Bem-vindo ao Planejador de Rotas Urbanas ---")
    try:
        num_locais = int(input("Digite o número de locais que você deseja registrar: "))
        if num_locais <= 0: print("O número de locais deve ser positivo."); return None
    except ValueError: print("Entrada inválida para o número de locais. Por favor, insira um número inteiro."); return None

    print("\n--- Registrando os Nomes dos Locais ---")
    for i in range(num_locais):
        while True:
            nome_local = input(f"Digite o nome do local {i}: ").strip()
            if not nome_local: print("O nome do local não pode ser vazio. Tente novamente.")
            elif nome_local in mapa_nome_para_id: print(f"O local '{nome_local}' já foi registrado. Use um nome diferente.")
            else:
                mapa_id_para_nome.append(nome_local)
                mapa_nome_para_id[nome_local] = i
                grafo[i] = []
                print(f"Local '{nome_local}' registrado com ID {i}.")
                break
    
    print("\n--- Inserindo as Rotas e Tempos de Viagem ---")
    print("Para cada local, insira os locais diretamente conectados e o tempo de viagem em minutos.")
    print("Formato para cada conexão: 'nome do local vizinho tempo_em_minutos' (ex: 'Mercado 15').")
    print("Digite 'fim' quando terminar de adicionar conexões para um local.")

    for id_atual, nome_atual in enumerate(mapa_id_para_nome):
        print(f"\nDefinindo rotas a partir de '{nome_atual}' (ID: {id_atual}):")
        while True:
            entrada_rota = input(f"  Adicionar rota de '{nome_atual}' para (ou 'fim'): ").strip()
            if entrada_rota.lower() == 'fim': break
            try:
                partes = entrada_rota.rsplit(' ', 1)
                if len(partes) != 2: raise ValueError("Formato incorreto. Use 'nome_local_vizinho tempo_viagem'.")
                
                nome_vizinho, tempo_str = partes[0].strip(), partes[1]
                tempo_viagem = int(tempo_str)

                if nome_vizinho not in mapa_nome_para_id: print(f"  Erro: Local vizinho '{nome_vizinho}' não reconhecido. Verifique os locais registrados."); continue
                id_vizinho = mapa_nome_para_id[nome_vizinho]

                if id_vizinho == id_atual: print(f"  Erro: Não é possível conectar um local a ele mesmo ('{nome_atual}')."); continue
                if tempo_viagem < 0: print("  Erro: O tempo de viagem não pode ser negativo."); continue
                
                if any(conn[0] == id_vizinho for conn in grafo[id_atual]):
                    print(f"  Aviso: Já existe uma rota de '{nome_atual}' para '{nome_vizinho}'. Ignorando esta entrada."); continue

                grafo[id_atual].append((id_vizinho, tempo_viagem))
                print(f"  Adicionado: Rota de '{nome_atual}' -> '{nome_vizinho}' em {tempo_viagem} minutos.")
            except ValueError as e:
                print(f"  Erro na entrada: {'O tempo de viagem deve ser um número.' if 'invalid literal for int()' in str(e) else e}. Tente novamente.")
            except Exception as e: print(f"  Ocorreu um erro inesperado: {e}. Tente novamente.")
    
    print("\n--- Mapa de Rotas Inserido ---")
    for id_local, conexoes in grafo.items():
        nome_local_origem = mapa_id_para_nome[id_local]
        conexoes_formatadas = [f"'{mapa_id_para_nome[id_viz]}' ({tempo} min)" for id_viz, tempo in conexoes]
        print(f"De '{nome_local_origem}': [{', '.join(conexoes_formatadas)}]")
    print("-----------------------------")
    return grafo, mapa_id_para_nome, mapa_nome_para_id

def construir_grafo_nao_direcionado(grafo_direcionado):
    todos_vertices = set(grafo_direcionado.keys()).union(*(set(v for v, _ in conns) for conns in grafo_direcionado.values()))
    grafo_nao_direcionado = {u: [] for u in todos_vertices}

    for u, conexoes in grafo_direcionado.items():
        for v, peso in conexoes:
            if (v, peso) not in grafo_nao_direcionado[u]: grafo_nao_direcionado[u].append((v, peso))
            if (u, peso) not in grafo_nao_direcionado[v]: grafo_nao_direcionado[v].append((u, peso))
    return grafo_nao_direcionado

def dijkstra(grafo, origem_id):
    distancias = {v_id: float('inf') for v_id in grafo}
    predecessores = {v_id: None for v_id in grafo}
    distancias[origem_id] = 0
    pq = [(0, origem_id)]

    while pq:
        dist_atual, u = heapq.heappop(pq)
        if dist_atual > distancias[u]: continue

        for v, peso in grafo.get(u, []):
            nova_distancia = dist_atual + peso
            if nova_distancia < distancias[v]:
                distancias[v] = nova_distancia
                predecessores[v] = u
                heapq.heappush(pq, (nova_distancia, v))
    return distancias, predecessores

def reconstruir_caminho_ids(predecessores, destino_id, origem_id, distancias):
    if distancias.get(destino_id, float('inf')) == float('inf') and destino_id != origem_id:
        return []
    
    caminho_ids = []
    atual_id = destino_id

    while atual_id is not None:
        caminho_ids.insert(0, atual_id) 
        if atual_id == origem_id: 
            break
        atual_id = predecessores.get(atual_id) 
    
    if not caminho_ids or caminho_ids[0] != origem_id:
        return [] 
        
    return caminho_ids

def prim(grafo_nao_direcionado, num_vertices):
    if not grafo_nao_direcionado: return []

    min_peso = {v: float('inf') for v in range(num_vertices)}
    predecessor = {v: None for v in range(num_vertices)}
    mst_set = [False] * num_vertices
    
    start_node = next((k for k in sorted(grafo_nao_direcionado.keys()) if grafo_nao_direcionado[k]), -1)
    if start_node == -1 and num_vertices > 0: print("Aviso: Nenhum nó com arestas para iniciar a MST."); return []
    if start_node == -1: return []

    min_peso[start_node] = 0
    pq = [(0, start_node)]
    mst_arestas, num_arestas_mst = [], 0

    while pq and num_arestas_mst < num_vertices - 1:
        peso_u, u = heapq.heappop(pq)
        if mst_set[u]: continue
        
        mst_set[u] = True
        if predecessor[u] is not None:
            mst_arestas.append((predecessor[u], u, peso_u))
            num_arestas_mst += 1

        for v, peso_uv in grafo_nao_direcionado.get(u, []):
            if not mst_set[v] and peso_uv < min_peso[v]:
                min_peso[v] = peso_uv
                predecessor[v] = u
                heapq.heappush(pq, (peso_uv, v))
    
    vertices_ativos = sum(1 for v in grafo_nao_direcionado if grafo_nao_direcionado[v] or any(u_id for u_id, _ in grafo_nao_direcionado.items() for u, _ in grafo_nao_direcionado[u_id] if u == v))
    if num_arestas_mst == vertices_ativos - 1: return mst_arestas
    elif vertices_ativos == 1 and num_arestas_mst == 0: return []
    else: print("\nAviso: O grafo não é completamente conectado. A MST foi gerada apenas para o componente conectado da origem. Se o grafo tem mais de um componente, a MST não incluirá todos os vértices."); return mst_arestas

if __name__ == "__main__":
    dados_grafo = obter_grafo()
    if not dados_grafo or not dados_grafo[0]: print("Não foi possível criar o mapa de rotas. Encerrando o programa."); exit()
    
    grafo_urbano, id_para_nome, nome_para_id = dados_grafo
    grafo_nao_direcionado_prim = construir_grafo_nao_direcionado(grafo_urbano)
    num_locais_total = len(id_para_nome)

    while True:
        print("\n--- Escolha uma Opção ---")
        print("1. Consultar Rota Mais Rápida (Dijkstra)")
        print("2. Calcular Árvore Geradora Mínima (Prim)")
        print("3. Sair")
        escolha = input("Digite sua escolha (1, 2 ou 3): ").strip()

        if escolha == '1':
            print("\n--- Consultar Rota Mais Rápida ---")
            try:
                nome_origem = input("Digite o nome do LOCAL DE ORIGEM (ou 'sair'): ").strip()
                if nome_origem.lower() == 'sair': print("Encerrando a consulta de rotas."); continue
                if nome_origem not in nome_para_id: print(f"Local de origem '{nome_origem}' não reconhecido. Locais disponíveis: {', '.join(id_para_nome)}"); continue
                origem_id_usr = nome_para_id[nome_origem]

                nome_destino = input("Digite o nome do LOCAL DE DESTINO (ou 'sair'): ").strip()
                if nome_destino.lower() == 'sair': print("Encerrando a consulta de rotas."); continue
                if nome_destino not in nome_para_id: print(f"Local de destino '{nome_destino}' não reconhecido. Locais disponíveis: {', '.join(id_para_nome)}"); continue
                destino_id_usr = nome_para_id[nome_destino]
                
                distancias_calculadas, predecessores_calculados = dijkstra(grafo_urbano, origem_id_usr)

                print(f"\n--- Resultados da Rota ---")
                print(f"Tempos de viagem mais rápidos a partir de '{id_para_nome[origem_id_usr]}':")
                for id_local, nome_local_mapa in enumerate(id_para_nome):
                    tempo_viagem = distancias_calculadas.get(id_local, float('inf'))
                    print(f"Para '{nome_local_mapa}': {'Inalcançável' if tempo_viagem == float('inf') else f'{tempo_viagem} minutos'}")
                
                print(f"\nCaminho mais rápido de '{id_para_nome[origem_id_usr]}' até '{id_para_nome[destino_id_usr]}':")
                caminho_em_ids = reconstruir_caminho_ids(predecessores_calculados, destino_id_usr, origem_id_usr, distancias_calculadas)

                if caminho_em_ids:
                    caminho_em_nomes = [id_para_nome[id_node] for id_node in caminho_em_ids]
                    print(" -> ".join(caminho_em_nomes))
                    tempo_total_viagem = distancias_calculadas.get(destino_id_usr, "N/A")
                    print(f"Tempo total de viagem: {tempo_total_viagem} minutos")
                else: print(f"Não existe rota direta ou indireta de '{id_para_nome[origem_id_usr]}' para '{id_para_nome[destino_id_usr]}'.")
            except Exception as e: print(f"Ocorreu um erro durante a consulta de rota: {e}")
        
        elif escolha == '2':
            print("\n--- Calculando a Árvore Geradora Mínima (MST) ---")
            mst_arestas = prim(grafo_nao_direcionado_prim, num_locais_total)
            if mst_arestas:
                custo_total_mst = sum(peso for u, v, peso in mst_arestas)
                print("\nArestas da Árvore Geradora Mínima (MST):")
                for u, v, peso in mst_arestas: print(f"  {id_para_nome[u]} --({peso} min)-- {id_para_nome[v]}")
                print(f"\nCusto total da MST: {custo_total_mst} minutos")
            else: print("Não foi possível calcular a MST. Verifique se o grafo está vazio, tem apenas um nó ou não é conectado.")
        
        elif escolha == '3': print("Encerrando o programa."); break
        else: print("Escolha inválida. Por favor, digite 1, 2 ou 3.")