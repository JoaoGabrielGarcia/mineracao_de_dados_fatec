"""Exercicio 2 - Calcula o IQR, os limites e verifica o valor 150."""

import numpy as np


dados = [12, 15, 14, 13, 16, 12, 14, 150, 13, 15]
q1, q3 = np.percentile(dados, [25, 75])
iqr = q3 - q1
margem = 1.5 * iqr
limite_inferior = q1 - margem
limite_superior = q3 + margem
valor = 150

print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"1.5 * IQR: {margem}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")
print(f"{valor} e candidato a outlier: {valor < limite_inferior or valor > limite_superior}")
