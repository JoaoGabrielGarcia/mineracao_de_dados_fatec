"""Exercicio 7 - Calcula o IQR de uma coluna de um DataFrame."""

import pandas as pd


dados = {
    "ID_Maquina": [1, 2, 3, 4, 5],
    "Uso_Memoria_MB": [2048, 2100, 2050, 8192, 2080],
}
df = pd.DataFrame(dados)
coluna = df["Uso_Memoria_MB"]
q1 = coluna.quantile(0.25)
q3 = coluna.quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
candidatos = df.loc[
    (coluna < limite_inferior) | (coluna > limite_superior), "Uso_Memoria_MB"
].tolist()

print(df)
print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")
print(f"Candidatos a outlier: {candidatos}")
