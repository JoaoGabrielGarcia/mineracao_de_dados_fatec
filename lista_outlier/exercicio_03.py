"""Exercicio 3 - Quartis pela mediana das metades, sem funcao pronta."""


def mediana(valores):
    quantidade = len(valores)
    meio = quantidade // 2
    if quantidade % 2 == 0:
        return (valores[meio - 1] + valores[meio]) / 2
    return valores[meio]


dados = [100, 150, 200, 250, 300, 350]
quantidade = len(dados)
meio = quantidade // 2

if quantidade % 2 == 0:
    metade_inferior = dados[:meio]
    metade_superior = dados[meio:]
else:
    metade_inferior = dados[:meio]
    metade_superior = dados[meio + 1 :]

q1 = mediana(metade_inferior)
q3 = mediana(metade_superior)
iqr = q3 - q1

print(f"Quantidade de elementos: {quantidade}")
print(f"Metade inferior: {metade_inferior}")
print(f"Metade superior: {metade_superior}")
print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
