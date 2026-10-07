"""Exercicio 9 - Substitui por mediana um outlier confirmado como erro."""

import numpy as np
import pandas as pd


temperaturas = [80, 82, 85, 81, 300, 83]
df = pd.DataFrame({"Temperatura": temperaturas})
q1 = df["Temperatura"].quantile(0.25)
q3 = df["Temperatura"].quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
mascara_outlier = (df["Temperatura"] < limite_inferior) | (
    df["Temperatura"] > limite_superior
)
mediana = df["Temperatura"].median()

df_corrigido = df.copy()
df_corrigido["Temperatura"] = np.where(
    mascara_outlier, mediana, df["Temperatura"]
)

print(f"Q1: {q1}; Q3: {q3}; IQR: {iqr}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")
print(f"Valores identificados: {df.loc[mascara_outlier, 'Temperatura'].tolist()}")
print(f"Mediana: {mediana}")
print("DataFrame antes da correcao:")
print(df)
print("\nDataFrame depois da correcao:")
print(df_corrigido)
