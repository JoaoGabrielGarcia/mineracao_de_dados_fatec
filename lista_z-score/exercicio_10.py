"""Exercicio 10 - Analisa tentativas de login com Pandas."""

import pandas as pd

dados = {
    "Evento": ["A", "B", "C", "D", "E", "F", "G"],
    "Tentativas_Login": [3, 4, 2, 5, 3, 4, 40],
}
df = pd.DataFrame(dados)
media = df["Tentativas_Login"].mean()
desvio = df["Tentativas_Login"].std(ddof=0)
df["Z_Score"] = (df["Tentativas_Login"] - media) / desvio

eventos_incomuns = df.loc[df["Z_Score"].abs() > 3]
print(f"Media de tentativas: {media:.2f}")
print(f"Desvio-padrao: {desvio:.2f}")
print("Z-Score de cada evento:")
print(df[["Evento", "Tentativas_Login", "Z_Score"]].to_string(index=False))
print("Eventos com |Z| > 3:")
if eventos_incomuns.empty:
    print("Nenhum evento ultrapassou o criterio pratico |Z| > 3.")
else:
    print(eventos_incomuns[["Evento", "Tentativas_Login", "Z_Score"]].to_string(index=False))
print(
    "Um evento incomum em seguranca pode ser o dado mais importante da analise; "
    "o resultado deve ser investigado, nao apagado automaticamente."
)
