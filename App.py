# importando as bibliotecas
import json
import os
import time

# função para adicionar item na lista
def adicionar_item(compras, item, quantidade):
    compras[item] = quantidade

# função para remover itens da lista
def remover_item(compras, item):
    if item in compras:
        del compras[item]

# função para visualizar a lista 
def visualizar_compras(compras):
    for item, quantidade in compras.items():
        print(f"{item}: {quantidade}")
    print()
    print("Pressione enter para continuar")
    input()

# função para salvar a lista
def salvar_compras(compras, nome_arquivo):
    with open(f'C:/Users/felip/OneDrive/Área de Trabalho/codigos/App compras/{nome_arquivo}', "w") as arquivo:
        json.dump(compras, arquivo)

# função para visualisar as listas disponiveis 
def carregar_compras(nome_arquivo):
    with open(f'C:/Users/felip/OneDrive/Área de Trabalho/codigos/App compras/{nome_arquivo}', "r") as arquivo:
        return json.load(arquivo)

# função para excluir alguma lista 
def excluir_lista(nome_arquivo):
    os.remove((f'C:/Users/felip/OneDrive/Área de Trabalho/codigos/App compras/{nome_arquivo}'))
            
# função para gerenciar o menu 
def gerenciar_compras(compras, nome_arquivo=None):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("1 Adicionar item")
        print("2 Remover item")
        print("3 Visualizar lista")
        print("4 Salvar e sair")
        print("5 Sair sem salvar")
        print('6 Excluir lista')
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            item = input("Digite o nome do item: ")
            quantidade = int(input("Digite a quantidade: "))
            adicionar_item(compras, item, quantidade)
        elif escolha == "2":
            item = input("Digite o nome do item: ")
            remover_item(compras, item)
        elif escolha == "3":
            visualizar_compras(compras)
        elif escolha == "4":
            if nome_arquivo is None:
                nome_arquivo = input("Digite o nome do arquivo para salvar: ")
            if not nome_arquivo.endswith(".json"):
                nome_arquivo += ".json"
            salvar_compras(compras, nome_arquivo)
            break
        elif escolha == "5":
            break
        elif escolha == '6':
            excluir_lista(nome_arquivo)
            break
        else:
            print("Opção inválida")
            time.sleep(1)

# função do menu
def main(): 
    while True: 
        os.system("cls" if os.name == "nt" else "clear")
        print("1 Criar uma nova lista de compras")
        print("2 Carregar uma lista existente")
        print("3 Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            compras = {}
            gerenciar_compras(compras)

        elif escolha == "2":
            print("Listas disponíveis:")
            arquivos = [arquivo for arquivo in os.listdir('C:/Users/felip/OneDrive/Área de Trabalho/codigos/App compras') if arquivo.endswith(".json")]
            if not arquivos:
                print("Nenhuma lista encontrada")
                time.sleep(2)
                continue
            for i, arquivo in enumerate(arquivos, 1):
                print(f"{i} {arquivo}")
            escolha = int(input("Escolha uma lista para carregar (0 se nenhuma): "))
            if escolha == 0:
                continue
            if escolha < 0 or escolha > len(arquivos):
                print("Opção inválida")
                time.sleep(1)
                continue
            nome_arquivo = arquivos[escolha - 1]
            compras = carregar_compras(nome_arquivo)
            gerenciar_compras(compras, nome_arquivo)
                
        elif escolha == "3":
            break
        else:
            print("Opção inválida")
            time.sleep(1)


if __name__ == "__main__":
    main()
