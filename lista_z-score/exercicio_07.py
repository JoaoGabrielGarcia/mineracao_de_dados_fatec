"""Exercicio 7 - Interpreta Z-Scores conforme as regras da lista."""


def interpretar_z(z):
    if abs(z) > 3:
        return "Investigar"
    if z < 0:
        return "Abaixo da media"
    if z > 0:
        return "Acima da media"
    return "Na media"


valores_z = [-3.5, -1.2, 0, 0.8, 3.7]
for z in valores_z:
    print(f"Z-Score: {z:.1f} -> {interpretar_z(z)}")
