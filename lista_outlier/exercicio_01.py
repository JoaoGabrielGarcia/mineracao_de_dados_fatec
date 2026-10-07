"""Exercicio 1 - Calcula quartis usando NumPy."""

import numpy as np


dados = [12, 15, 14, 13, 16, 12, 14, 150, 13, 15]

q1, q2, q3 = np.percentile(dados, [25, 50, 75])

print(f"Q1 (percentil 25): {q1}")
print(f"Q2 (mediana / percentil 50): {q2}")
print(f"Q3 (percentil 75): {q3}")
