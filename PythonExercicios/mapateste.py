grafo = {
    'Beatriz': {'Bruno', 'Joel'},
    'Bruno': {'Beatriz', 'Davi'},
    'Joel': {'Beatriz', 'Davi'},
    'Davi': {'Bruno', 'Joel'}
}
#Grafo representado em dicionário
#Pra cada usuário um conjunto de amigos

def adicionar_usuario(grafo, usuario):
    # Adiciona um novo usuário no grafo
    if usuario not in grafo:
        grafo[usuario] = set()

def adicionar_amizade(grafo, usuario1, usuario2):
    # Adiciona uma relação de amizade entre os usuários
    grafo[usuario2].add(usuario1)
    grafo[usuario1].add(usuario2)

rede_social = {}

adicionar_usuario(rede_social, 'Beatriz')
adicionar_usuario(rede_social, 'Bruno')
adicionar_usuario(rede_social, 'Joel')
adicionar_usuario(rede_social, 'Davi')

adicionar_amizade(rede_social, 'Beatriz', 'Davi')
adicionar_amizade(rede_social, 'Bruno', 'Joel')
adicionar_amizade(rede_social, 'Davi', 'Beatriz')
adicionar_amizade(rede_social, 'Joel', 'Bruno')


print(rede_social)