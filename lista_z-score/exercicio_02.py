"""Exercicio 2 - Classifica valores em relacao a media."""

casos = [85, 100, 120]
media = 100
desvio = 10

for valor in casos:
    z_score = (valor - media) / desvio
    if z_score < 0:
        posicao = "abaixo da media"
    elif z_score > 0:
        posicao = "acima da media"
    else:
        posicao = "exatamente na media"
    print(f"Valor: {valor} -> Z-Score: {z_score:.2f} -> {posicao}")
