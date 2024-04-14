- [Notebook - Exemplos](graphhub/matplotlib/matplotlib.ipynb)

# Matplotlib.pyplot

O `matplotlib.pyplot` é um módulo no Matplotlib que fornece uma interface semelhante ao MATLAB para a criação de figuras. É através do `pyplot` que podemos criar gráficos e visualizações de dados de forma rápida e conveniente. Aqui estão alguns dos recursos principais:

- **Funções de plotagem**: O `pyplot` oferece uma variedade de funções para plotar diferentes tipos de gráficos, como `plot`, `scatter`, `bar`, `hist`, `pie`, entre outros.
- **Controle de estilo**: Permite personalizar o estilo dos gráficos com funções como `title`, `xlabel`, `ylabel`, `legend` e `grid`.
- **Gerenciamento de figura**: Com funções como `figure` e `subplot`, os usuários podem gerenciar múltiplas figuras e eixos.
- **Exibição e salvamento**: O módulo possibilita a exibição de figuras na tela com `show` e o salvamento em arquivos com `savefig`.
- **Interface interativa**: O `pyplot` também suporta uma interface interativa que permite aos usuários alterar figuras e atualizar gráficos em tempo real.

O `pyplot` é frequentemente usado por sua simplicidade e eficácia, sendo uma ferramenta essencial para cientistas de dados, engenheiros e analistas que precisam visualizar dados de maneira clara e informativa.

# Pacotes e Módulos do Matplotlib

Além do `pyplot`, o Matplotlib possui vários outros pacotes e módulos que oferecem funcionalidades diversas para a criação de gráficos. Aqui estão alguns dos pacotes principais:

- **`matplotlib.axes`**: Este módulo contém a classe `Axes`, que é a região da figura onde os dados são plotados.
- **`matplotlib.figure`**: Fornece a classe `Figure`, que é o contêiner de nível superior para todos os elementos do gráfico.
- **`matplotlib.animation`**: Permite a criação de animações dentro do Matplotlib.
- **`matplotlib.widgets`**: Contém ferramentas para adicionar widgets interativos à visualização de dados.
- **`matplotlib.backends`**: Inclui backends específicos para diferentes interfaces de usuário, como Qt, GTK, Tk ou para formatos de arquivo como PDF ou PNG.

# Matplotlib e sua Interface

O `matplotlib.pyplot` não é uma classe, mas sim um módulo que fornece uma interface para a biblioteca Matplotlib que imita a funcionalidade do MATLAB. Ele é projetado para ser interativo e permite que os usuários criem figuras e gráficos de forma rápida e conveniente.

As outras classes, como `Figure`, `Axes`, entre outras, são parte da arquitetura orientada a objetos do Matplotlib e podem ser utilizadas diretamente para um controle mais fino e personalização avançada dos gráficos.

## Explicação Simplificada

- **`matplotlib.pyplot`**: É o módulo que contém funções que permitem criar e manipular figuras e eixos de forma procedural (semelhante ao MATLAB). Por exemplo, quando você chama `plt.plot()`, o `pyplot` automaticamente cria uma figura e um eixo se eles ainda não existirem.
- **`matplotlib.figure.Figure`**: É a classe que representa a figura inteira, o contêiner de nível superior para todos os elementos do gráfico. Uma figura pode conter vários eixos.
- **`matplotlib.axes.Axes`**: É a classe que representa os eixos de um gráfico. Cada conjunto de eixos pode conter vários tipos de gráficos e é onde a maior parte da personalização do gráfico acontece.

Portanto, enquanto `pyplot` é usado para tarefas de plotagem mais simples e diretas, as classes como `Figure` e `Axes` oferecem mais controle e são usadas para personalizações mais complexas e detalhadas. Em muitos casos, especialmente em scripts e programas maiores, os desenvolvedores preferem usar a interface orientada a objetos para ter um controle mais granular sobre os elementos do gráfico.

