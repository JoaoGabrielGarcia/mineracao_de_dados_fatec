"""Exercicio 10 - Compara a dispersao central de dois grupos."""

import numpy as np


grupo_a = [48, 49, 50, 50, 51, 52, 52, 53]
grupo_b = [20, 30, 40, 50, 60, 70, 80, 90]


def quartis_e_iqr(grupo):
    q1, q3 = np.percentile(grupo, [25, 75])
    return q1, q3, q3 - q1


q1_a, q3_a, iqr_a = quartis_e_iqr(grupo_a)
q1_b, q3_b, iqr_b = quartis_e_iqr(grupo_b)

print(f"Grupo A: Q1={q1_a}, Q3={q3_a}, IQR={iqr_a}")
print(f"Grupo B: Q1={q1_b}, Q3={q3_b}, IQR={iqr_b}")
print("Maior IQR: grupo B" if iqr_b > iqr_a else "Maior IQR: grupo A")
