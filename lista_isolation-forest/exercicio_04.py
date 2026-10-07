import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import IsolationForest

# Cada linha representa [passageiros, atraso em minutos].
viagens = np.array([
    [32, 3], [45, 5], [50, 4],
    [60, 6], [55, 5], [70, 7],
    [65, 6], [80, 8], [75, 7],
    [10, 45],
])

modelo = IsolationForest(
    n_estimators=100,
    contamination=1 / len(viagens),
    random_state=42,
)
rotulos = modelo.fit_predict(viagens)

print("Colunas: passageiros, atraso_minutos")
print(viagens)
print("Rotulos (1 = normal; -1 = candidato a anomalia):", rotulos)
print("Viagens sinalizadas [passageiros, atraso_minutos]:\n", viagens[rotulos == -1])

normais = rotulos == 1
plt.figure(figsize=(8, 5))
plt.scatter(viagens[normais, 0], viagens[normais, 1], label="Normal", color="royalblue")
plt.scatter(viagens[~normais, 0], viagens[~normais, 1], label="Candidata a anomalia", color="darkorange", marker="x", s=100)
plt.xlabel("Numero de passageiros")
plt.ylabel("Atraso (minutos)")
plt.title("Passageiros e atraso por viagem")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
