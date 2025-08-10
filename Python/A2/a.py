# Grafo não direcionado e ponderado (cidades de SP)
grafo_sp = {
    # São Paulo (1)
    "São Paulo": [
        ("Guarulhos", 20), ("Osasco", 16), ("Santo André", 18), 
        ("São Bernardo do Campo", 22), ("Campinas", 93)
    ],
    # Campinas (2)
    "Campinas": [
        ("São Paulo", 93), ("Jundiaí", 42), ("Piracicaba", 63), 
        ("Americana", 22), ("Sorocaba", 120)
    ],
    # Guarulhos (3)
    "Guarulhos": [
        ("São Paulo", 20), ("São José dos Campos", 80), ("Itaquaquecetuba", 15)
    ],
    # São Bernardo do Campo (4)
    "São Bernardo do Campo": [
        ("São Paulo", 22), ("Santo André", 10), ("Santos", 58)
    ],
    # Santo André (5)
    "Santo André": [
        ("São Paulo", 18), ("São Bernardo do Campo", 10), ("Mauá", 12)
    ],
    # Osasco (6)
    "Osasco": [
        ("São Paulo", 16), ("Barueri", 8)  # Barueri não está na lista original
    ],
    # Ribeirão Preto (7)
    "Ribeirão Preto": [
        ("Franca", 100), ("Araraquara", 110), ("São José do Rio Preto", 210)
    ],
    # Sorocaba (8)
    "Sorocaba": [
        ("Campinas", 120), ("Itaquaquecetuba", 140), ("Bauru", 230)
    ],
    # Santos (9)
    "Santos": [
        ("São Bernardo do Campo", 58), ("Praia Grande", 15)  # Praia Grande não está na lista
    ],
    # São José dos Campos (10)
    "São José dos Campos": [
        ("Guarulhos", 80), ("Taubaté", 40), ("Jacareí", 20)  # Jacareí não está na lista
    ],
    # Bauru (11)
    "Bauru": [
        ("Sorocaba", 230), ("Marília", 90), ("Araçatuba", 170)
    ],
    # Piracicaba (12)
    "Piracicaba": [
        ("Campinas", 63), ("Rio Claro", 50), ("Limeira", 30)  # Limeira e Rio Claro não estão na lista
    ],
    # Taubaté (13)
    "Taubaté": [
        ("São José dos Campos", 40), ("Pindamonhangaba", 15)  # Pindamonhangaba não está na lista
    ],
    # Itaquaquecetuba (14)
    "Itaquaquecetuba": [
        ("Guarulhos", 15), ("Sorocaba", 140), ("Poá", 8)  # Poá não está na lista
    ],
    # São José do Rio Preto (15)
    "São José do Rio Preto": [
        ("Ribeirão Preto", 210), ("Araçatuba", 180), ("Araraquara", 160)
    ],
    # Franca (16)
    "Franca": [
        ("Ribeirão Preto", 100), ("Araraquara", 120)
    ],
    # Presidente Prudente (17)
    "Presidente Prudente": [
        ("Araçatuba", 240), ("Marília", 150)
    ],
    # Araçatuba (18)
    "Araçatuba": [
        ("Bauru", 170), ("São José do Rio Preto", 180), ("Presidente Prudente", 240)
    ],
    # Araraquara (19)
    "Araraquara": [
        ("Ribeirão Preto", 110), ("Franca", 120), ("São José do Rio Preto", 160)
    ],
    # Marília (20)
    "Marília": [
        ("Bauru", 90), ("Presidente Prudente", 150)
    ],
    # Jundiaí (21)
    "Jundiaí": [
        ("Campinas", 42), ("São Paulo", 60)
    ],
    # Americana (22)
    "Americana": [
        ("Campinas", 22), ("Piracicaba", 40)
    ]
}

# Exemplo de como acessar as conexões e pesos
print("Conexões de Campinas:")
for cidade, peso in grafo_sp["Campinas"]:
    print(f"  → {cidade} ({peso} km)")

# Saída esperada:
# Conexões de Campinas:
#   → São Paulo (93 km)
#   → Jundiaí (42 km)
#   → Piracicaba (63 km)
#   → Americana (22 km)
#   → Sorocaba (120 km)