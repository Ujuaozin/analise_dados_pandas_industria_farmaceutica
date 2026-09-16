import pandas as pd
import numpy as np

np.random.seed(42)
n = 120

data = {
    "lote_id": [f"LT-{1000 + i}" for i in range(n)],
    "linha_producao": np.random.choice(["Linha_A", "Linha_B", "Linha_C", None], size=n, p=[0.35, 0.35, 0.25, 0.05]),
    "temperatura_reator_c": np.random.normal(loc=36.5, scale=1.2, size=n).round(2),
    "rendimento_pct": np.random.choice([85.4, 92.1, 78.0, 99.5, -5.0, 150.0, np.nan], size=n),
    "unidades_produzidas": np.random.choice(["10000", "12500", "8000", "invalid_read", "15000"], size=n),
    "data_inicio": pd.date_range(start="2026-01-01", periods=n, freq="D").astype(str),
    "status_aprovacao": np.random.choice(["Aprovado", "Reprovado", "Em Quarentena"], size=n, p=[0.75, 0.15, 0.10])
}

df = pd.DataFrame(data)
df = pd.concat([df, df.iloc[:3]], ignore_index=True) # duplicatas intencionais
df.to_csv("lotes_producao.csv", index=False)
print("Arquivo lotes_producao.csv pronto!")