"""Exercicio 5 - Funcao reutilizavel para detectar candidatos a outlier."""

import numpy as np


def detectar_anomalias(dados, multiplicador):
    """Retorna quartis, IQR, limites e valores fora dos limites do IQR."""
    q1, q3 = np.percentile(dados, [25, 75])
    iqr = q3 - q1
    limite_inferior = q1 - multiplicador * iqr
    limite_superior = q3 + multiplicador * iqr
    candidatos = [
        valor for valor in dados
        if valor < limite_inferior or valor > limite_superior
    ]
    return q1, q3, iqr, limite_inferior, limite_superior, candidatos
