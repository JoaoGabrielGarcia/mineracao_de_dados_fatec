import numpy as np
from sklearn.ensemble import IsolationForest

# Cada observacao representa a quantidade de produtos vendidos em um dia.
vendas = np.array([
    [80], [85], [90], [88],
    [92], [87], [95], [89],
    [91], [400],
])

modelo = IsolationForest(
    n_estimators=100,
    contamination=1 / len(vendas),
    random_state=42,
)
rotulos = modelo.fit_predict(vendas)

print("Vendas:", vendas[:, 0])
print("Rotulos (1 = normal; -1 = candidato a anomalia):", rotulos)
print("Vendas sinalizadas:", vendas[rotulos == -1, 0])
