import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import IsolationForest

# Cada linha representa [distancia percorrida (km), litros consumidos].
consumo = np.array([
    [10, 1.0], [20, 1.8], [30, 2.6],
    [40, 3.5], [50, 4.3], [60, 5.1],
    [70, 6.0], [80, 7.0], [90, 8.0],
    [100, 20.0],
])

modelo = IsolationForest(
    n_estimators=100,
    contamination=1 / len(consumo),
    random_state=42,
)
rotulos = modelo.fit_predict(consumo)

print("Colunas: distancia_km, litros")
print(consumo)
print("Rotulos (1 = normal; -1 = candidato a anomalia):", rotulos)
print("Combinacoes sinalizadas [km, litros]:\n", consumo[rotulos == -1])

normais = rotulos == 1
plt.figure(figsize=(8, 5))
plt.scatter(consumo[normais, 0], consumo[normais, 1], label="Normal", color="seagreen")
plt.scatter(consumo[~normais, 0], consumo[~normais, 1], label="Candidato a anomalia", color="crimson", marker="x", s=100)
plt.xlabel("Distancia percorrida (km)")
plt.ylabel("Combustivel consumido (litros)")
plt.title("Consumo de combustivel por distancia")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
