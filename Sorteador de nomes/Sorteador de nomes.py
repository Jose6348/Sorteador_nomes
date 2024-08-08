import random

# Função para adicionar nomes e temas
def adicionar_elementos(lista, tipo):
    while True:
        elemento = input(f"Digite um {tipo} (ou 'sair' para finalizar): ").strip()
        if elemento.lower() == 'sair':
            break
        lista.append(elemento)

# Função para sortear temas para os nomes
def sortear_temas(nomes, temas):
    random.shuffle(temas)  # Embaralha a lista de temas
    if len(nomes) > len(temas):
        print("Aviso: Há mais nomes do que temas, alguns nomes ficarão sem temas.")
    sorteio = {}
    for i, nome in enumerate(nomes):
        if i < len(temas):
            sorteio[nome] = temas[i]
        else:
            sorteio[nome] = "Sem tema disponível"
    return sorteio

# Listas para armazenar os nomes e temas
nomes = []
temas = []

print("Adicione os nomes dos participantes:")
adicionar_elementos(nomes, "nome")

print("Adicione os temas de trabalho:")
adicionar_elementos(temas, "tema")

# Sorteio dos temas para os nomes
sorteio = sortear_temas(nomes, temas)

# Exibir o resultado do sorteio
print("\nResultado do sorteio:")
for nome, tema in sorteio.items():
    print(f"{nome} - {tema}")
