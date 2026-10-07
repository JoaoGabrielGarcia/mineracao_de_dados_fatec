"""Exercicio 9 - Compara os limites do IQR e o Z-Score."""

import numpy as np

dados = [10, 11, 12, 12, 13, 13, 14, 15, 30]
q1, q3 = np.percentile(dados, [25, 75])
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
media = np.mean(dados)
desvio = np.std(dados)
valor = 30
z_score = (valor - media) / desvio

print(f"Q1: {q1:.2f}; Q3: {q3:.2f}; IQR: {iqr:.2f}")
print(f"Limite inferior do IQR: {limite_inferior:.2f}")
print(f"Limite superior do IQR: {limite_superior:.2f}")
print(f"Media: {media:.2f}; desvio-padrao: {desvio:.2f}")
print(f"Z-Score de {valor}: {z_score:.2f}")
print(f"IQR sinaliza {valor}: {valor < limite_inferior or valor > limite_superior}")
print(f"Criterio |Z| > 3 sinaliza {valor}: {abs(z_score) > 3}")
