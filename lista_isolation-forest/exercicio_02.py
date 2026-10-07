import numpy as np
from sklearn.ensemble import IsolationForest

# Latencias em milissegundos: a maioria e baixa, com duas observacoes elevadas.
latencias = np.array([
    [24], [28], [31], [35], [38], [42], [45],
    [49], [53], [58], [62], [67], [230], [280],
])

modelo = IsolationForest(
    n_estimators=100,
    contamination=2 / len(latencias),
    random_state=42,
)
rotulos = modelo.fit_predict(latencias)

print("Latencias (ms):", latencias[:, 0])
print("Rotulos (1 = normal; -1 = candidato a anomalia):", rotulos)
print("Latencias sinalizadas (ms):", latencias[rotulos == -1, 0])
