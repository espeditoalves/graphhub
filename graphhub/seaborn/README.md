
[Notebook: Figure-level vs. axes-level functions](seaborn_figure_axes_level.ipynb)

- [Figure-level vs. axes-level functions](#figure-level-vs-axes-level-functions)
  - [Axes-level function:](#axes-level-function)
  - [Figure-level function:](#figure-level-function)


# Figure-level vs. axes-level functions

Na biblioteca `Seaborn`, as funções são classificadas em dois tipos principais: funções de nível de figura **(figure-level)** e funções de nível de eixo **(axes-level)**.

## Axes-level function:

- As **axes-level function** operam em um único objeto `matplotlib.pyplot.Axes`. Isso significa que elas desenham os dados em um único conjunto de eixos (ou seja, um único gráfico ou subplot).
- Exemplos de **axes-level function** incluem `sns.histplot`, `sns.kdeplot`, entre outras.
Essas funções são úteis quando você quer um controle mais fino sobre a aparência específica de um gráfico e está trabalhando com um layout de subplot personalizado.

## Figure-level function:

- As **figure-level function** criam uma nova figura e podem gerar múltiplos gráficos em uma única figura.
Elas interagem com o Matplotlib por meio de um objeto do Seaborn, geralmente um `FacetGrid`, que gerencia a figura inteira.
- Exemplos de **figure-level function** incluem `sns.displot`, `sns.catplot`, `sns.relplot`, entre outras.
Essas funções são particularmente úteis quando você deseja criar gráficos complexos com múltiplos subplots de maneira fácil e consistente.
Em resumo, se você precisa de um gráfico simples ou está ajustando um subplot específico, uma função de nível de eixo pode ser a escolha certa. Por outro lado, se você quer criar uma figura com múltiplos gráficos ou precisa de uma maneira conveniente de explorar diferentes aspectos dos seus dados, uma função de nível de figura será mais apropriada1.
