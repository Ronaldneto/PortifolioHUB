# TaskTracker — Projeto de Gerenciamento de Tarefas

**Bootcamp II — Fase 2: Entrega Intermediária**

## 1. Visão geral

O TaskTracker é uma aplicação de linha de comando (CLI), desenvolvida em Python 3, com o objetivo de permitir o cadastro e a visualização de tarefas. O projeto faz parte do Bootcamp II e representa a implementação prática do planejamento lógico elaborado na Fase 1.

## 2. Objetivo do projeto

Transformar o planejamento lógico em uma aplicação funcional, aplicando conceitos de lógica de programação, estruturação de dados, funções, validação de entradas e versionamento de código com Git e GitHub.

## 3. Funcionalidades

A aplicação disponibiliza um menu interativo com as seguintes opções:

1. **Cadastrar nova tarefa:** registra uma tarefa com título, descrição, prioridade e data limite.
2. **Visualizar tarefas cadastradas:** apresenta as tarefas registradas e suas respectivas informações.
3. **Sair da aplicação:** encerra o programa.

## 4. Regras de negócio e validações

Cada tarefa possui os seguintes campos:

- **Título:** obrigatório; não permite valores vazios ou compostos apenas por espaços.
- **Descrição:** permite registrar detalhes sobre a tarefa.
- **Prioridade:** aceita exclusivamente Alta, Média (ou Media) e Baixa.
- **Data limite:** registra a data planejada para conclusão, preferencialmente no formato DD/MM/AAAA.
- **Status:** definido automaticamente como Pendente no momento do cadastro.

Quando o usuário informa um título vazio ou uma prioridade inválida, o sistema apresenta uma mensagem de erro e solicita uma nova entrada.

Caso não existam tarefas cadastradas, a aplicação informa que não há registros disponíveis.

## 5. Tecnologias utilizadas

- Python 3: desenvolvimento da lógica e das funcionalidades.
- Git: controle de versão e registro da evolução do código.
- GitHub: hospedagem do repositório e apresentação do histórico de desenvolvimento.
- Visual Studio Code: ambiente de edição e execução do código.

## 6. Estrutura do projeto

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## 7. Como executar

1. Instale o Python 3 no computador.
2. Abra o terminal na pasta principal do projeto.
3. Execute o seguinte comando:

```bash
python src/main.py
```

No Windows, caso necessário, utilize:

```bash
py src/main.py
```

Após a execução, o menu será exibido no terminal. Basta selecionar a opção desejada e informar os dados solicitados.

## 8. Versionamento e controle de alterações

O desenvolvimento utiliza Git para registrar a evolução do projeto por meio de commits. O repositório no GitHub permite acompanhar a estrutura dos arquivos e as alterações realizadas durante a implementação.

## 9. Limitações atuais

As tarefas são armazenadas temporariamente em memória durante a execução. Ao encerrar o programa, os registros não são preservados. A persistência de dados poderá ser considerada em futuras evoluções do projeto.

## 10. Próximas etapas

A Fase 3 prevê a continuidade do desenvolvimento, com empacotamento da aplicação, containerização com Docker, testes e implantação (deploy), conforme o planejamento do Bootcamp II.<img width="1611" height="884" alt="image" src="https://github.com/user-attachments/assets/063d5ac3-d185-408e-a0a5-2f87515a379e" />
