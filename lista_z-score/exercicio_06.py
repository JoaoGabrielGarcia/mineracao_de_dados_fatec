"""Exercicio 6 - Compara o mesmo valor em dois grupos."""

media_a = 100
desvio_a = 2
media_b = 100
desvio_b = 20
valor = 110

z_a = (valor - media_a) / desvio_a
z_b = (valor - media_b) / desvio_b

print(f"Z-Score no Grupo A: {z_a:.2f}")
print(f"Z-Score no Grupo B: {z_b:.2f}")
print(f"Comparacao: |Z_A| = {abs(z_a):.2f} e |Z_B| = {abs(z_b):.2f}.")
