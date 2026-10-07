from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import IsolationForest

arquivo = Path(__file__).resolve().parent / "sensores_ambientais.csv"
dados = pd.read_csv(arquivo)
print("Primeiras linhas:")
print(dados.head())

caracteristicas = ["temperatura", "umidade"]
modelo = IsolationForest(
    n_estimators=100,
    contamination=3 / len(dados),
    random_state=42,
)
dados["rotulo"] = modelo.fit_predict(dados[caracteristicas])

print("\nLeituras candidatas:")
print(dados.loc[dados["rotulo"] == -1, ["id_leitura", *caracteristicas, "rotulo"]])

normais = dados["rotulo"] == 1
plt.figure(figsize=(8, 5))
plt.scatter(dados.loc[normais, "temperatura"], dados.loc[normais, "umidade"], label="Normal", color="seagreen")
plt.scatter(dados.loc[~normais, "temperatura"], dados.loc[~normais, "umidade"], label="Candidata a anomalia", color="crimson", marker="x", s=100)
plt.xlabel("Temperatura (°C)")
plt.ylabel("Umidade (%)")
plt.title("Leituras dos sensores ambientais")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
