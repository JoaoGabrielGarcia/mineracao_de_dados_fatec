"""Exercicio 8 - Calcula Z-Score em um DataFrame."""

import numpy as np
import pandas as pd

dados = {
    "Usuario": ["ana", "bruno", "carla", "diego", "eva", "fabio"],
    "Requisicoes": [120, 135, 128, 122, 130, 400],
}
df = pd.DataFrame(dados)
media = df["Requisicoes"].mean()
desvio = np.std(df["Requisicoes"])
df["Z_Score"] = (df["Requisicoes"] - media) / desvio
df["Status"] = np.where(df["Z_Score"].abs() > 3, "Investigar", "Comum")

print(f"Media de Requisicoes: {media:.2f}")
print(f"Desvio-padrao: {desvio:.2f}")
print("Linhas marcadas para investigacao:")
print(df.loc[df["Status"] == "Investigar"].to_string(index=False))
