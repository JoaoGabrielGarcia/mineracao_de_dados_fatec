import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import IsolationForest

# Contexto: acessos a um site por hora.
# Cada linha representa [requisicoes, erros_http].
acessos = np.array([
    [42, 1], [48, 2], [51, 1], [55, 2], [46, 1], [59, 3],
    [62, 2], [53, 1], [45, 2], [57, 2], [50, 1], [64, 3],
    [49, 2], [60, 1], [54, 2], [47, 1],
    [180, 4],   # Pico de acessos: pode ser campanha ou evento legitimo.
    [52, 38],   # Muitos erros: pode indicar falha ou ataque.
])

modelo = IsolationForest(
    n_estimators=100,
    contamination=2 / len(acessos),
    random_state=42,
)
rotulos = modelo.fit_predict(acessos)

print("Colunas: requisicoes, erros_http")
print(acessos)
print("Rotulos (1 = normal; -1 = candidato a anomalia):", rotulos)
print("Observacoes sinalizadas [requisicoes, erros_http]:\n", acessos[rotulos == -1])

normais = rotulos == 1
plt.figure(figsize=(8, 5))
plt.scatter(acessos[normais, 0], acessos[normais, 1], label="Normal", color="teal")
plt.scatter(acessos[~normais, 0], acessos[~normais, 1], label="Candidato a anomalia", color="crimson", marker="x", s=100)
plt.xlabel("Requisicoes por hora")
plt.ylabel("Erros HTTP por hora")
plt.title("Acessos e erros do site")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
