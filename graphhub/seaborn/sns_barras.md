# Diferenças entre Countplot, Histplot e Barplot do SEABORN

## Countplot

O `countplot` é usado para contar a frequência de observações em uma variável categórica. Ele exibe o número de ocorrências de cada categoria usando barras verticais.

- **Eixo x**: A variável categórica é plotada no eixo x.
- **Eixo y**: O eixo y mostra a contagem de observações para cada categoria.
- **Uso**: Ideal para variáveis categóricas simples ou para comparar a distribuição de categorias.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Exemplo de dados
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'A', 'C', 'C', 'B']
}

df = pd.DataFrame(data)

# Plotando um countplot
sns.countplot(x='Category', data=df)
plt.show()
```

## Histplot

O `histplot` é usado para visualizar a distribuição de uma variável numérica usando barras verticais.

- **Eixo x:** A variável numérica é plotada no eixo x.
- **Eixo y:** O eixo y mostra a contagem de observações dentro de cada intervalo (bin).
- **Uso:** Útil para entender a distribuição e a forma da distribuição de dados numéricos.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Gerando dados aleatórios
np.random.seed(0)
data = np.random.normal(loc=0, scale=1, size=100)

# Plotando um histplot
sns.histplot(data=data, bins=10)
plt.show()
```

## Barplot

O barplot é usado para comparar quantidades entre diferentes grupos.

- **Eixo x:** Os grupos são geralmente plotados no eixo x.
- **Eixo y:** A variável numérica é plotada no eixo y.
- **Uso:** Útil para comparar quantidades entre diferentes categorias ou grupos.
  
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Exemplo de dados
data = {
    'Category': ['A', 'B', 'C'],
    'Value': [10, 15, 8]
}

df = pd.DataFrame(data)

# Plotando um barplot
sns.barplot(x='Category', y='Value', data=df)
plt.show()
```

### Principais Diferenças
**Variáveis de Entrada:**

- **Countplot:** Uma variável categórica no eixo x.
- **Histplot:** Uma variável numérica no eixo x.
- **Barplot:** Uma variável categórica ou de agrupamento no eixo x e uma variável numérica no eixo y.

### Propósito:

- **Countplot**: Contar a frequência de categorias.
- **Histplot**: Visualizar a distribuição de uma variável numérica.
- **Barplot**: Comparar quantidades entre categorias ou grupos.

### Visualização:

**Countplot** e **Barplot** usam barras verticais para representar as contagens ou valores.
**Histplot** usa barras verticais (histograma) para representar a distribuição dos dados.




