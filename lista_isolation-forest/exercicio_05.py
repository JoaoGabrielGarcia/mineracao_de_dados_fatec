import numpy as np
from sklearn.ensemble import IsolationForest

consumo_agua = np.array([
    [48], [52], [50], [55],
    [49], [53], [51], [54],
    [56], [12], [180],
])

# Regra fixa definida para este exemplo: sinaliza consumo abaixo de 40 ou acima de 70.
limite_inferior = 40
limite_superior = 70
sinalizado_regra = (consumo_agua[:, 0] < limite_inferior) | (consumo_agua[:, 0] > limite_superior)

modelo = IsolationForest(
    n_estimators=100,
    contamination=2 / len(consumo_agua),
    random_state=42,
)
rotulos = modelo.fit_predict(consumo_agua)
sinalizado_modelo = rotulos == -1

print("Consumos (litros):", consumo_agua[:, 0])
print("Regra fixa (< 40 ou > 70):", consumo_agua[sinalizado_regra, 0])
print("Isolation Forest:", consumo_agua[sinalizado_modelo, 0])
print("Rotulos do modelo (1 = normal; -1 = candidato a anomalia):", rotulos)
print("Candidatos iguais?", set(consumo_agua[sinalizado_regra, 0]) == set(consumo_agua[sinalizado_modelo, 0]))
