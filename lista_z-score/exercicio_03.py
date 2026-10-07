"""Exercicio 3 - Encontra as leituras mais distantes da media."""

temperaturas = [21, 23, 25, 27, 29]
media = 25
desvio = 2
resultados = []

for temperatura in temperaturas:
    z_score = (temperatura - media) / desvio
    resultados.append((temperatura, z_score))
    print(f"Temperatura: {temperatura} -> Z-Score: {z_score:.2f}")

maior_abs_z = max(abs(z_score) for _, z_score in resultados)
mais_distantes = [
    temperatura
    for temperatura, z_score in resultados
    if abs(z_score) == maior_abs_z
]
print(f"Maior valor absoluto de Z: {maior_abs_z:.2f}")
print(f"Leitura(s) mais distante(s) da media: {mais_distantes}")
