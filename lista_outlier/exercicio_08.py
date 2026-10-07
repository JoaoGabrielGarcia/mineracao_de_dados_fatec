"""Exercicio 8 - Marca outliers em uma coluna do DataFrame."""

import pandas as pd


dados = {
    "Pedido": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Valor": [100, 120, 110, 130, 125, 115, 140, 1000],
}
df = pd.DataFrame(dados)
q1 = df["Valor"].quantile(0.25)
q3 = df["Valor"].quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
df["Outlier"] = (df["Valor"] < limite_inferior) | (df["Valor"] > limite_superior)

print(f"Q1: {q1}; Q3: {q3}; IQR: {iqr}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")
print("DataFrame completo:")
print(df)
print("\nLinhas marcadas como outlier:")
print(df.loc[df["Outlier"]])
