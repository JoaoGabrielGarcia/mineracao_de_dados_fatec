from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import IsolationForest

arquivo = Path(__file__).resolve().parent / "vendas_ecommerce.csv"
dados = pd.read_csv(arquivo)
print("Primeiras linhas:")
print(dados.head())

# O identificador da venda nao e uma caracteristica comportamental.
caracteristicas = ["valor_total", "quantidade_itens", "desconto_percentual"]
modelo = IsolationForest(
    n_estimators=100,
    contamination=3 / len(dados),
    random_state=42,
)
dados["rotulo"] = modelo.fit_predict(dados[caracteristicas])

print("\nVendas candidatas:")
print(dados.loc[dados["rotulo"] == -1, ["id_venda", *caracteristicas, "rotulo"]])

normais = dados["rotulo"] == 1
plt.figure(figsize=(8, 5))
plt.scatter(dados.loc[normais, "quantidade_itens"], dados.loc[normais, "valor_total"], label="Normal", color="royalblue")
plt.scatter(dados.loc[~normais, "quantidade_itens"], dados.loc[~normais, "valor_total"], label="Candidata a anomalia", color="darkorange", marker="x", s=100)
plt.xlabel("Quantidade de itens")
plt.ylabel("Valor total")
plt.title("Vendas: valor total e quantidade de itens")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
