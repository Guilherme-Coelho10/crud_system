import json
import os

animes = "dados.json"

def menu():
    print("""
------MENU------
1 - Listar
2 - Criar
3 - Ler por ID
4 - Atualizar
5 - Deletar
6 - Filtrar
0 - Sair""")
    
def carregar():
    if not os.path.exists(animes):
        return []
    with open("dados.json", "r", encoding="utf-8") as arq:
        try:
            return json.load(arq)
        except:
            return []
        
def salvar(lista):
    with open(animes, "w", encoding="utf-8") as arq:
            json.dump(lista, arq, indent=2, ensure_ascii=False)



def criar(lista, titulo, genero, desc, eps, status):
    new_id = len(lista) + 1
    lista.append({"id": new_id, "titulo": titulo,
                  "genero": genero, "descrição": desc,
                  "epísodios": eps, "status": status})
    
    print({"id": new_id, "titulo": titulo,
                  "genero": genero, "descrição": desc,
                  "epísodios": eps, "status": status})
    
    salvar(lista)

def listar(lista):
    for item in lista:
        print(f"id={item['id']} \ntitulo={item['titulo']} \ngenero={item['genero']} \ndescrição={item['descrição']} \nepísodios={item['epísodios']} \nstatus={item['status']}")

        print("-" * 40)

def ler_id(id, lista):
    print()
    if 0 <= (id - 1) <= len(lista):
        for k,v in lista[id-1].items():
            print(f"{k}: {v}")
    else:
        print("ID desconhecido.")



def atualizar(lista, id):
    if 0 <= (id - 1) < len(lista):
        for k in lista[id-1].keys():
            if k == "id":
                continue

            novo = input(f"{k} (ENTER para manter): ")
            if novo != "":
                if k == "genero":
                    lista[id-1][k] = novo.split()
                else:
                    lista[id-1][k] = novo
                
        salvar(lista)

    else:
        print("ID desconhecido!")

def deletar(id, lista):
    ids = [item["id"] for item in lista]
    if id in ids:
        ind = ids.index(id)
        del lista[ind]
        salvar(lista)
    else:
        print("ID desconhecido!")

def filtrar(lista):
    print("1 - Genero \n2 - Status")
    opc = int(input("> "))
    if opc == 1:
        genre = input("Genêro: ")
        for i in range(len(lista)):
            if genre in lista[i]["genero"]:
                print(lista[i])

    elif opc == 2:
        stts = input("Status: ")
        for i in range(len(lista)):
            if lista[i]["status"] == stts:
                print(lista[i])

    else:
        print("Opção inválida!")

#-----------Progrma Principal--------------
while True:
    dados = carregar()
    menu()
    opc = int(input("> "))
    print()
    if opc == 1:
        listar(dados)

    elif opc == 2:

        title = input("Titulo: ")
        genre = input("Genêro: ")
        desc = input("Descrição: ")
        eps = int(input("Episódios: "))
        stats = input("Status: ")

        generos = genre.split()
        verify = [title, desc, stats]
        campo_vazio = 0
        for item in verify:
            if not item.strip():
                campo_vazio += 1

        if not generos:
            campo_vazio += 1

        if campo_vazio == 0 and eps > 0:
            criar(dados, title, generos, desc, eps, stats)
        else:
            print("Campos obrigátorios. Digite corretamente.")
        

    elif opc == 3:
        try:
            id_escolhido = int(input("ID: "))
        except ValueError:
            print("ID inválido. Digite um número inteiro positivo.")
        
        if id_escolhido > 0:
            ler_id(id_escolhido, dados)
        
        else:
            print("ID inexistente. Não há ID negativo ou ID 0.")

    elif opc == 4:
        ID = int(input("ID: "))
        atualizar(dados, ID)

    elif opc == 5:
        id = int(input("ID: "))
        deletar(id, dados)

    elif opc == 6:
        filtrar(dados)

    elif opc == 0:
        break

    else:
        print("Opção inválida! Tente novamente.")






