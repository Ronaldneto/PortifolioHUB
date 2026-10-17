
def cadastrar_tarefa(tarefas):
    print("\n--- CADASTRAR NOVA TAREFA ---")

    while True:
        titulo = input("Titulo: ").strip()
        if titulo:
            break
        print("Erro: o titulo nao pode ficar vazio.")

    descricao = input("Descricao: ").strip()

    while True:
        prioridade = input(
            "Prioridade (Alta, Media ou Baixa): "
        ).strip().lower()

        prioridades = {
            "alta": "Alta",
            "media": "Media",
            "média": "Media",
            "baixa": "Baixa"
        }

        if prioridade in prioridades:
            prioridade = prioridades[prioridade]
            break

        print("Erro: escolha Alta, Media ou Baixa.")

    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def visualizar_tarefas(tarefas):
    print("\n--- TAREFAS CADASTRADAS ---")

    if not tarefas:
        print("Nao existem tarefas cadastradas.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"Titulo: {tarefa['titulo']}")
        print(f"Descricao: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")


def main():
    tarefas = []

    while True:
        print("\n===== TASKTRACKER =====")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("Encerrando o TaskTracker.")
            break
        else:
            print("Opcao invalida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()

