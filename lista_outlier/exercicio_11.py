"""Exercicio 11 - Mostra boxplot e identifica candidatos pela Regra do IQR."""

import matplotlib.pyplot as plt
import numpy as np


tempos = [20, 21, 22, 23, 24, 25, 26, 80]
q1, q3 = np.percentile(tempos, [25, 75])
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
candidatos = [
    valor for valor in tempos
    if valor < limite_inferior or valor > limite_superior
]

print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")
print(f"Candidatos a outlier: {candidatos}")

plt.boxplot(tempos)
plt.ylabel("Tempo")
plt.title("Boxplot dos tempos")
plt.show()
