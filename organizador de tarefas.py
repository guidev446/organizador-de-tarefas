import json
import os

arquivo = "dados.json"

if os.path.exists(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)
        tarefas = dados.get("tarefas", [])
        pesquisas = dados.get("pesquisas", [])
else:
    tarefas = []
    pesquisas = []

def salvar():
    dados = {
        "tarefas": tarefas,
        "pesquisas": pesquisas
    }

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)


print("organizador de tarefas")
print()

while True:

    print("====abas====")
    print("adicionar tarefa")
    print("ver tarefas")
    print("marca deveres como  conluidas/remover")
    print("pesquisas")
    print("sair")

    aba = input("qual aba voce quer entrar")

    if aba == "adicionar tarefa":
        trf = input("marque a tarefa assim:materia/paginas/dia de entrega")
        tarefas.append(trf)
        salvar()
        print("tarefa adicionada")

    elif aba == "ver tarefas":
        print(tarefas)

    elif aba == "marca deveres como  conluidas/remover":
        print(tarefas)
        remover = input("qual tarefa concluída")
        tarefas.remove(remover)
        salvar()
        print("tarefa concluida")

    elif aba == "pesquisas":
        pesqisa = input("voce quer adicionar uma pesquisa ou ver(escreva adicionar pesquisas ou ver pesquisas)")

        if pesqisa == "ver pesquisas":
            print(pesquisas)

        elif pesqisa == "adicionar pesquisas":
            sla = input("qual pesquisa escreva assim:materia/paginas/dia de entrega")
            pesquisas.append(sla)
            salvar()

    if aba == "sair":
        print("espero que voce faça o seu dever")
        break