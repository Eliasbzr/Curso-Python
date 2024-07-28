# LISTA DE TAREFAS

# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os, json

def listar (tarefas):
    print()
    if not tarefas:
        print('Nada para listar')
        return #esse return para a funcao aqui, e não executa os comandos abaixo
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t {tarefa}')


def desfazer (tarefas, tarefa_desfeita):
    print()
    if not tarefas:
        print('Nada para desfazer')
        print()
        return #esse return para a funcao aqui, e não executa os comandos abaixo
    
    tarefa = tarefas.pop()
    print(f'Tarefa excluida: {tarefa}')
    tarefa_desfeita.append(tarefa)
    print()


def refazer (tarefas, tarefa_desfeita):
    print()
    if not tarefa_desfeita:
        print('Nada para refazer')
        print()
        return #esse return para a funcao aqui, e não executa os comandos abaixo
    
    tarefa = tarefa_desfeita.pop()
    print(f'Refazendo Tarefa: {tarefa}')
    tarefas.append(tarefa)
    print()

def salvar (tarefas, caminho_arquivo):
    dados = tarefas
  
    with open (caminho_arquivo, 'w+', encoding='utf8') as arquivo:
        json.dump(
            tarefas,
            arquivo,
            ensure_ascii=False,
            indent=2,
        )
    return dados

def ler (tarefas, caminho_arquivo):
    dados = []
    try:
        with open (caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


CAMINHO_ARQUIVO = 'tarefas.json'
tarefas =ler([], CAMINHO_ARQUIVO)
tarefa_desfeita= []




while True:
    tarefa = input('Digite uma ação ou tarefa \n'
                    'Ações: [l]istar | [r]efazer | [d]esfazer | [e]ncerrar | [c]lear | [s]alvar \n')

    if tarefa.lower() == 'l':
        listar(tarefas) 
        continue

    elif tarefa.lower() == 'd':
        desfazer(tarefas, tarefa_desfeita)
        continue

    elif tarefa.lower()=='r':
        refazer(tarefas, tarefa_desfeita)
        continue

    elif tarefa.lower()=='c':
        os.system('cls')
        continue

    elif tarefa.lower()=='e':
        print('Saindo...')
        break 
    elif tarefa.lower()=='ler':
        ler(tarefas, CAMINHO_ARQUIVO)

    elif tarefa.lower()=='s':
        salvar(tarefas)

    else:
        tarefas.append(tarefa)
        continue




