"""Exercicio 4 - Avalia a latencia de 180 ms com NumPy."""

import numpy as np

latencias = [98, 102, 101, 99, 100, 103, 97, 180]
media = np.mean(latencias)
desvio = np.std(latencias)  # Desvio-padrao populacional do conjunto.
latencia = 180
z_score = (latencia - media) / desvio

print(f"Media: {media:.2f} ms")
print(f"Desvio-padrao: {desvio:.2f} ms")
print(f"Z-Score de {latencia} ms: {z_score:.2f}")
if abs(z_score) > 3:
    print("A latencia merece investigacao (|Z| > 3).")
else:
    print("A latencia nao ultrapassa o criterio pratico |Z| > 3.")
print("Investigar um valor nao significa apaga-lo automaticamente.")
