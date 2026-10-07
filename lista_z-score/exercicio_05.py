"""Exercicio 5 - Classifica leituras de CPU com NumPy."""

import numpy as np

cpu = [42, 45, 47, 44, 46, 43, 48, 92]
media = np.mean(cpu)
desvio = np.std(cpu)  # Desvio-padrao populacional do conjunto.

print(f"Media: {media:.2f}")
print(f"Desvio-padrao: {desvio:.2f}")
for leitura in cpu:
    z_score = (leitura - media) / desvio
    classificacao = "Investigar" if abs(z_score) > 3 else "Comum"
    print(f"{leitura} -> {z_score:.2f} -> {classificacao}")
