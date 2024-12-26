Gerenciador de Tarefas

Este aplicativo permitirá que você:

● Adicionar novas tarefas com título, descrição e data de conclusão.
● Listar todas as tarefas, categorizando-as como pendentes ou concluídas.
● Marcar tarefas como concluídas.
● Remover tarefas.
● Salvar e carregar tarefas de um arquivo para garantir persistência de dados entre
execuções.
● Pesquisar tarefas por título ou descrição.
● Ordenar tarefas por data de conclusão.

Objetivos do Projeto
● Integrar Conceitos: Utilizar estruturas de dados, manipulação de arquivos, funções
e tratamento de exceções.
● Desenvolver Habilidades Práticas: Aprender a estruturar um programa maior e
mais funcional.
● Melhorar a Organização do Código: Utilizar funções para modularizar o código e
torná-lo mais legível.
● Aprender Novas Técnicas: Implementar funcionalidades adicionais como pesquisa
e ordenação.

Funcionalidades Principais
1. Adicionar Tarefa
○ Entrada: Título, descrição e data de conclusão.
○ Ação: Criar uma nova tarefa e adicioná-la à lista de tarefas.

2. Listar Tarefas
○ Exibir todas as tarefas, categorizando-as como pendentes ou concluídas.

3. Marcar Tarefa como Concluída
○ Entrada: ID da tarefa.
○ Ação: Atualizar o status da tarefa para concluída.

4. Remover Tarefa
○ Entrada: ID da tarefa.
○ Ação: Remover a tarefa da lista.

5. Salvar e Carregar Tarefas
○ Salvar: Escrever a lista de tarefas em um arquivo JSON.
○ Carregar: Ler a lista de tarefas do arquivo JSON.

6. Pesquisar Tarefas
○ Entrada: Termo de pesquisa.
○ Ação: Filtrar tarefas que contenham o termo no título ou descrição.

7. Ordenar Tarefas por Data
○ Ação: Ordenar a lista de tarefas com base na data de conclusão.

Estrutura de Dados
Utilizaremos uma lista para armazenar as tarefas, onde cada tarefa será um dicionário
com as seguintes chaves:
● 'id': Identificador único da tarefa.
● 'titulo': Título da tarefa.
● 'descricao': Descrição detalhada.
● 'data': Data de conclusão.
● 'concluida': Booleano indicando se a tarefa foi concluída.