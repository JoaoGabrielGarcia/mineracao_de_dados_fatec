"""Exercicio 1 - Distancia em passos de desvio-padrao."""

media = 100
desvio = 5
valor = 115

distancia = valor - media
z_score = distancia / desvio

print(f"Distancia entre o valor e a media: {distancia}")
print(f"Z-Score: {z_score:.2f}")
print(
    f"O valor {valor} esta {abs(z_score):.0f} desvios-padrao acima da media."
)
