
# Seaborn

- [Seaborn](#seaborn)
- [Figure-level vs. axes-level functions](#figure-level-vs-axes-level-functions)
  - [Axes-level function:](#axes-level-function)
  - [Figure-level function:](#figure-level-function)
- [Resumo Principais funções do seaborn](#resumo-principais-funções-do-seaborn)
  - [`sns.histplot()`](#snshistplot)
- [Configurações de Estilo no Seaborn](#configurações-de-estilo-no-seaborn)
  - [`sns.set_theme()`](#snsset_theme)
  - [`sns.axes_style()`](#snsaxes_style)
  - [`sns.set_style()`](#snsset_style)
  - [`sns.plotting_context()`](#snsplotting_context)
  - [`sns.set_context()`](#snsset_context)
  - [`sns.set_color_codes()`](#snsset_color_codes)
  - [`sns.reset_defaults()`](#snsreset_defaults)
  - [`sns.reset_orig()`](#snsreset_orig)
  - [`sns.set()`](#snsset)

# Figure-level vs. axes-level functions

[Notebook: Figure-level vs. axes-level functions](seaborn_figure_axes_level.ipynb)

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

`Figure-level functions` não podem (facilmente) ser compostas com outros gráficos. Por design, eles “possuem” sua própria figura, incluindo sua inicialização, portanto <span style="color:red">**não faz sentido usar uma Figure-level functions para desenhar um gráfico em eixos existentes**</span>. 

# Resumo Principais funções do seaborn

[Notebook: seaborn_exemplos](seaborn_exemplos.ipynb)

## `sns.histplot()`

A função `sns.histplot` da biblioteca Seaborn em Python é utilizada para criar histogramas, que são gráficos que exibem a distribuição de um conjunto de dados contínuos ou categóricos.
Ao plotar o gráfico essa função conta a quantidade de registros do dataframe e plota.

```python
# Importando a biblioteca Seaborn
import seaborn as sns

# sns.histplot é chamada com os seguintes parâmetros principais:
sns.histplot(
    data,           # DataFrame contendo os dados
    x=None,         # Nome da coluna no DataFrame para o eixo x
    y=None,         # Nome da coluna no DataFrame para o eixo y (opcional)
    hue=None,       # Nome da coluna para agrupar os dados por cores
    bins='auto',    # Número de bins ou uma sequência de bins
    kde=False,      # Se True, adiciona uma estimativa de densidade kernel (KDE)
    stat='count',   # A função agregada para y ('count', 'frequency', 'density', 'probability')
    cumulative=False # Se True, cria um histograma cumulativo
)

# Exemplo de uso:
sns.histplot(data=penguins, x="flipper_length_mm", hue="species")

```

- **data**: O DataFrame que contém os dados a serem plotados.
- **x e y**: Especificam as colunas do DataFrame que serão usadas nos eixos x e y do gráfico.
- **hue**: Permite a separação dos dados por categorias, representadas por cores diferentes no histograma.
- **bins**: Define o número de barras (bins) no histograma. Pode ser um número fixo, uma sequência de valores ou ‘auto’ para um cálculo automático.
- **kde**: Se ativado, adiciona uma linha de Estimativa de Densidade Kernel ao gráfico, que ajuda a visualizar a forma da distribuição.
- **stat**: Determina a função agregada para os dados no eixo y, como ‘count’, ‘frequency’, ‘density’, ou ‘probability’.
- **cumulative**: Se verdadeiro, os bins acumulam os valores anteriores, resultando em um histograma cumulativo.

O processo de contagem que o `seaborn` faz internamente é semelhate ao `grupby` do pandas.

```python
# Sem hue
df.groupby(['variavel']).size().reset_index(name='contagem')
# Com hue
df.groupby(['variavel1', 'variavel2']).size().reset_index(name='contagem')
```

# Configurações de Estilo no Seaborn

[Notebook-seaborn_theme](seaborn_theme.ipynb)

## `sns.set_theme()`

Esta função configura os aspectos do tema visual para todos os gráficos do Matplotlib e Seaborn. Ela altera os padrões globais usando o sistema `rcParams` do Matplotlib. Você pode definir o contexto, estilo, paleta, fonte, escala da fonte e códigos de cores.

## `sns.axes_style()`

Retorna um dicionário com os parâmetros de estilo dos eixos. É útil para obter ou definir temporariamente o estilo dos eixos para um gráfico específico.

```python
{'axes.facecolor': 'white',
 'axes.edgecolor': 'black',
 'axes.grid': False,
 'axes.axisbelow': 'line',
 'axes.labelcolor': 'black',
 'figure.facecolor': 'white',
 'grid.color': '#b0b0b0',
 'grid.linestyle': '-',
 'text.color': 'black',
 'xtick.color': 'black',
 'ytick.color': 'black',
 'xtick.direction': 'out',
 'ytick.direction': 'out',
 'lines.solid_capstyle': <CapStyle.projecting: 'projecting'>,
 'patch.edgecolor': 'black',
 'patch.force_edgecolor': False,
 'image.cmap': 'viridis',
 'font.family': ['sans-serif'],
 'font.sans-serif': ['DejaVu Sans',
  'Bitstream Vera Sans',
  'Computer Modern Sans Serif',
  'Lucida Grande',
  'Verdana',
  'Geneva',
  'Lucid',
  'Arial',
  'Helvetica',
  'Avant Garde',
  'sans-serif'],
 'xtick.bottom': True,
 'xtick.top': False,
 'ytick.left': True,
 'ytick.right': False,
 'axes.spines.left': True,
 'axes.spines.bottom': True,
 'axes.spines.right': True,
 'axes.spines.top': True}
```

## `sns.set_style()`

Define o estilo estético dos eixos dos gráficos. É uma forma de configurar a aparência dos gráficos mais permanentemente.

## `sns.plotting_context()`

Retorna um dicionário com os parâmetros de contexto de plotagem. Isso inclui coisas como o tamanho das fontes, linhas e outros elementos do gráfico.

## `sns.set_context()`

Permite ajustar os parâmetros de contexto de plotagem, como o tamanho das fontes e linhas para se adequar a diferentes contextos (por exemplo, papéis, palestras, pôsteres, etc.).

## `sns.set_color_codes()`

Se ativado e a paleta for uma paleta do Seaborn, remapeia os códigos de cores abreviados (como "b", "g", "r", etc.) para as cores dessa paleta. É útil quando você deseja usar códigos de cores consistentes com a paleta atual.

## `sns.reset_defaults()`

Redefine os parâmetros para os padrões do Matplotlib. Isso é útil se você modificou os padrões e deseja voltar ao original.

## `sns.reset_orig()`

Semelhante ao `sns.reset_defaults()`, mas redefinirá os parâmetros para os padrões originais do Matplotlib que estavam em vigor antes da importação do Seaborn.

## `sns.set()`

Uma função mais antiga que era usada para configurar os parâmetros estéticos dos gráficos. Em versões mais recentes do Seaborn, `sns.set_theme()` é preferido para essa finalidade.

Essas funções são usadas para controlar a estética dos gráficos criados com Seaborn e Matplotlib, permitindo que você personalize a aparência de acordo com suas necessidades ou preferências. Cada função tem um propósito específico, seja para definir estilos, ajustar o contexto de plotagem ou redefinir para os padrões.