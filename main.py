import pandas as pd

# 1. Carregar o arquivo
df = pd.read_csv("lotes_producao.csv")

df = df.drop_duplicates()
df["linha_producao"] = df["linha_producao"].fillna("Não Informado")
df_validos = df[(df["rendimento_pct"] >= 0) & (df["rendimento_pct"] <= 100)].copy()


df_validos["data_inicio"] = pd.to_datetime(df_validos["data_inicio"], errors="coerce")
df_validos["ano"] = df_validos["data_inicio"].dt.year
df_validos["mes"] = df_validos["data_inicio"].dt.month
df_validos["dia_semana"] = df_validos["data_inicio"].dt.day_name()


print("--- 1. VISUALIZANDO AS PRIMEIRAS LINHAS ---")
print(df_validos.head())
print("\n--- 2. RAIO-X DAS COLUNAS (INFO) ---")
df_validos.info()
print("\n--- 3. CONTAGEM DE VALORES NULOS POR COLUNA ---")
print(df_validos.isna().sum())



# Convertendo a coluna unidades_produzidas para número forçadamente
df_validos["unidades_produzidas"] = pd.to_numeric(df_validos["unidades_produzidas"], errors="coerce")
df_validos = df_validos.dropna(subset=["unidades_produzidas"]).copy()


print("\n--- DEPOIS DA CONVERSÃO DE UNIDADES PRODUZIDAS ---")
print("Novo tipo da coluna:", df_validos["unidades_produzidas"].dtype)

print("\n --- RENDIMENTO MÉDIO DAS LINHAS DE PRODUÇÃO ---")
print(df_validos.groupby("linha_producao")["rendimento_pct"].agg(["mean", "count"]))



print("\n--- RESUMO ESTATÍSTICO (DESCRIBE) ---")
print(df_validos.describe())



print("\n --- UNIDADES EFETIVAS --- ")
df_validos["unidades_efetivas"] = df_validos["unidades_produzidas"] * df_validos["rendimento_pct"] / 100
print(df_validos[["lote_id", "unidades_efetivas"]].head())

print("\n --- SOMA DAS UNIDADES EFETIVAS POR LINHA DE PRODUÇÃO --- ")
print(df_validos.groupby("linha_producao")["unidades_efetivas"].sum())


print("\n --- RENDIMENTOS POR DIA DA SEMANA --- ")
print(df_validos.groupby("dia_semana")["rendimento_pct"].agg(["mean", "count"]))


print("\n --- COEFICIENTE DE CORRELAÇÃO DE PEARSON --- ")
correlacao = df_validos["temperatura_reator_c"].corr(df_validos["rendimento_pct"])
print(f"Correlação entre Temperatura e Rendimento: {correlacao:.2f}")
print("\n Interpretação de Correlação entre as Colunas: \n +1.0 = Correlação positiva forte \n 0.0 = Correlação Neutra \n -1.0 = Correlação negativa forte")

df_validos.to_csv("lotes_producao_tratados.csv", index=False)
print("\n✅ Base limpa exportada com sucesso como 'lotes_producao_tratados.csv'!")