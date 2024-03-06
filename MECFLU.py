#!/usr/bin/env python
# coding: utf-8

# # **1. Construindo as linhas de corrente para o seguinte campo de velocidades: V = (0,5 + 0,8x)i + (1,5 - 0,8y)j**
#  (x e y estão dados em metros; os valores de x e y devem ambos variando entre -5 e 5)
# 

# In[65]:


# Importa as bibliotecas NumPy e Matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Define a função para calcular o campo de velocidades
def velocity_field(x, y):
    # Componente de velocidade u (horizontal)
    u = 0.5 + 0.8 * x
    # Componente de velocidade v (vertical)
    v = 1.5 - 0.8 * y
    return u, v

# Cria uma grade de pontos ao longo dos eixos x e y
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Calcula as velocidades em cada ponto da grade
U, V = velocity_field(X, Y)

# Normaliza as velocidades para criar as linhas de corrente
U_normalized = U / np.sqrt(U*U + V*V)
V_normalized = V / np.sqrt(U*U + V*V)

# Plota as linhas de corrente usando as coordenadas e as velocidades normalizadas
plt.streamplot(X, Y, U_normalized, V_normalized, density=2, linewidth=1, color='blue')

# Configura os limites do gráfico
plt.xlim(-5, 5)
plt.ylim(-5, 5)

# Adiciona um título e rótulos dos eixos
plt.title('Linhas de Corrente do Campo de Velocidades')
plt.xlabel('X (metros)')
plt.ylabel('Y (metros)')

# Mostra o gráfico
plt.show()


# # **2. Determinando o campo de aceleração associado ao campo de velocidade do item 1**

# In[66]:


import sympy as sp

# Defina a variável simbólica
x = sp.symbols('x')
y = sp.symbols('y')

# Defina a função para a qual deseja calcular a derivada
u = 0.5 + 0.8 * x
v = 1.5 - 0.8 * y

# Calcule a derivada da função em relação a x
f_prime_u = sp.diff(u, x)
f_prime_v = sp.diff(v, y)

# Achando as componentes da aceleração
ax = u * f_prime_u
ay = v * f_prime_v

# Imprima a derivada
print(f"O campo de aceleração é: ({ax})\u00EE + ({ay})ĵ")


# # **3. Calculando a velocidade no ponto (1,1)**
# 

# In[67]:


# Define as coordenadas do ponto onde desejamos calcular a velocidade
x_point = 1
y_point = 1

# Chama a função 'velocity_field' para calcular as componentes de velocidade no ponto (x_point, y_point)
u, v = velocity_field(x_point, y_point)

# Calcula a magnitude da velocidade usando o teorema de Pitágoras
magnitude = np.sqrt(u**2 + v**2)

# Imprime a magnitude da velocidade no ponto especificado
print(f"A magnitude da velocidade no ponto ({x_point}, {y_point}) é {magnitude:.3f}")


# # **5. Ponto(s) do domínio de análise onde a velocidade é zero**

# In[68]:


import sympy as sp

# Defina as variáveis simbólicas
x, y = sp.symbols('x y')

# Equações de velocidade
u = 0.5 + 0.8 * x
v = 1.5 - 0.8 * y

# Resolva as equações para u e v igual a zero
zero_velocity_x = sp.solve(u, x)
zero_velocity_y = sp.solve(v, y)

# Imprima os valores numéricos onde a velocidade é zero
print("Pontos onde a velocidade é zero:")
for x_val in zero_velocity_x:
    for y_val in zero_velocity_y:
        print(f"x = {x_val:.3f}, y = {y_val:.3f}")


# # **4. Calcular a aceleração no ponto (1,1)**

# In[72]:


import sympy as sp

# Substitua os valores de x e y no ponto (1, 1)
x_value = 1
y_value = 1

# Calcule as derivadas em relação a x e y
f_prime_u = sp.diff(u, x)
f_prime_v = sp.diff(v, y)

# Calcule as componentes da aceleração em (1, 1)
ax = u * f_prime_u
ay = v * f_prime_v
print(ax)
print(ay)
# Substitua os valores de x e y no ponto (1, 1)
ax_at_point = ax.subs({x: x_value, y: y_value})
ay_at_point = ay.subs({x: x_value, y: y_value})
print(ax_at_point**2)
print (ay_at_point**2)
# Calcule a magnitude da aceleração
magnitude_acceleration = sp.sqrt(ax_at_point**2 + ay_at_point**2)

# Imprima a magnitude da aceleração no ponto (1, 1)
print(f"A magnitude da aceleração no ponto ({x_value}, {y_value}) é: {magnitude_acceleration:.3f}")

