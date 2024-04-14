- [tetse](#graphhub/pages/matplotlib.md)
Exemplo 1: Uso simples com matplotlib.pyplot

Este exemplo usa o módulo pyplot para criar um gráfico de linha simples de forma rápida e direta:
import matplotlib.pyplot as plt

# Dados para plotagem
x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]

# Criação rápida de um gráfico de linha
plt.plot(x, y)
plt.title('Gráfico de Linha Simples')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()


Exemplo 2: Uso avançado com a interface orientada a objetos

Este exemplo utiliza a interface orientada a objetos para criar uma figura com dois subplots, cada um com sua própria personalização:

import matplotlib.pyplot as plt
import numpy as np

# Dados para plotagem
x = np.linspace(0, 2, 100)
y1 = np.sin(2 * np.pi * x)
y2 = np.cos(2 * np.pi * x)

# Criação da figura e dos eixos
fig, (ax1, ax2) = plt.subplots(2, 1)  # 2 linhas, 1 coluna

# Primeiro subplot
ax1.plot(x, y1, 'r-')  # Linha vermelha
ax1.set_title('Seno')
ax1.set_ylabel('Amplitude')

# Segundo subplot
ax2.plot(x, y2, 'b--')  # Linha tracejada azul
ax2.set_title('Cosseno')
ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel('Amplitude')

# Ajuste automático do layout para evitar sobreposições
plt.tight_layout()
plt.show()

