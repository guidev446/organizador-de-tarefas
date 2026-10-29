
import json
import os

from winotify import Notification

notificacao = Notification(
    app_id="Organizador de Tarefas",
    title="📚 Hora do dever!",
    msg="Não esqueça de fazer suas tarefas!",
    duration="short"
)

notificacao.show()

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
    print("==== abas ====")
    print("adicionar tarefa")
    print("ver tarefas")
    print("marca deveres como concluidas/remover")
    print("pesquisas")
    print("sair")

    aba = input("qual aba voce quer entrar: ").lower().strip()

    if aba == "adicionar tarefa":
        trf = input("marque a tarefa assim: materia/paginas/dia de entrega: ").strip()
        tarefas.append(trf)
        salvar()
        print("tarefa adicionada")

    elif aba == "ver tarefas":
        print(tarefas)

    elif aba == "marca deveres como concluidas/remover":
        print(tarefas)
        remover = input("qual tarefa concluida: ").strip()

        if remover in tarefas:
            tarefas.remove(remover)
            salvar()
            print("tarefa removida")
        else:
            print("tarefa nao encontrada")

    elif aba == "pesquisas":
        pesquisa_opcao = input(
            "voce quer adicionar uma pesquisa ou ver pesquisas: "
        ).lower().strip()

        if pesquisa_opcao == "ver pesquisas":
            print(pesquisas)

        elif pesquisa_opcao == "adicionar pesquisas":
            pesquisa = input(
                "qual pesquisa? escreva assim: materia/paginas/dia de entrega: "
            ).strip()
            pesquisas.append(pesquisa)
            salvar()
            print("pesquisa adicionada")

        else:
            print("opcao invalida")

    elif aba == "sair":
        print("espero que voce faca o seu dever")
        break

    else:
        print("aba nao encontrada")
