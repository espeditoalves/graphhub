# Qual escolher: plt.rcParams.update() ou sns.set_theme()

## Consistência Global

O **`plt.rcParams.update()`** afeta todos os gráficos **matplotlib** e **seaborn** criados posteriormente na sessão, enquanto **`sns.set_theme()`**  configura apenas os gráficos do Seaborn. Se você está trabalhando com múltiplos pacotes de visualização ou quer garantir que todas as suas figuras tenham a mesma aparência globalmente, **`plt.rcParams.update()`** é uma escolha eficiente.

**Exemplo: ``plt.rcParams.update()``**
```sh
# Definindo os parâmetros globais
plt.rcParams.update({
    'font.family': 'serif',         # Fonte geral
    'font.serif': 'Times New Roman',# Estilo da fonte
    'font.size': 12,                # Tamanho da fonte
    'axes.labelsize': 12,           # Tamanho da fonte dos rótulos dos eixos
    'axes.titlesize': 14,           # Tamanho da fonte dos títulos dos subplots
    'xtick.labelsize': 10,          # Tamanho da fonte dos rótulos do eixo x
    'ytick.labelsize': 10,          # Tamanho da fonte dos rótulos do eixo y
    'legend.fontsize': 12,          # Tamanho da fonte da legenda
    'figure.titlesize': 16,         # Tamanho da fonte do título da figura
    'axes.spines.right': False,     # Remover a espinha do lado direito
    'axes.spines.top': False        # Remover a espinha do topo
})
```
**Exemplo: ``set_theme``**
```sh

# Define os parâmetros que deseja modificar
custom_params = {
    'font.family': 'serif',         # Fonte geral
    'font.serif': 'Times New Roman',# Estilo da fonte
    'font.size': 12,                # Tamanho da fonte
    'axes.labelsize': 12,           # Tamanho da fonte dos rótulos dos eixos
    'axes.titlesize': 14,           # Tamanho da fonte dos títulos dos subplots
    'xtick.labelsize': 10,          # Tamanho da fonte dos rótulos do eixo x
    'ytick.labelsize': 10,          # Tamanho da fonte dos rótulos do eixo y
    'legend.fontsize': 12,          # Tamanho da fonte da legenda
    'figure.titlesize': 16,         # Tamanho da fonte do título da figura
    "axes.spines.right": False,     # Remover a espinha do lado direito
    "axes.spines.top": False}       # Remover a espinha do topo

# Configura o tema do seaborn com o estilo "ticks" e os parâmetros customizados
sns.set_theme(style="darkgrid", rc=custom_params)

```

