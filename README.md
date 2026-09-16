# Análise de Eficiência e Rendimento em Lotes de Produção Farmacêutica

Projeto prático focado em Engenharia e Análise Exploratória de Dados (EDA) para a indústria farmacêutica. O objetivo é higienizar dados de sensores e logs de produção, identificar gargalos de processo e preparar a base para modelagem e dashboards no Power BI.

## Contexto de Negócio
A operação farmacêutica lida com parâmetros críticos de qualidade e rendimento. A base original continha ruídos típicos de chão de fábrica: falhas de sensores, duplicatas no log, rendimentos fisicamente impossíveis e falta de padronização nas datas.

## O que foi feito no Pipeline (Python & Pandas)
- **Limpeza de Duplicatas e Nulos:** Remoção de registros repetidos e tratamento de linhas de produção não preenchidas.
- **Validação de Regras de Negócio:** Filtragem de outliers de rendimento fora da faixa real (0% a 100%).
- **Tratamento de Tipos e Sensores:** Conversão forçada de leituras corrompidas de unidades produzidas e descarte controlado de dados sem medição confiável.
- **Engenharia de Variáveis Temporais:** Padronização de datas para extração de ano, mês e dia da semana.
- **Métricas Derivadas:** Cálculo do volume efetivo real produzido (`unidades_efetivas`).
- **Análise Estatística e Correlação:** Avaliação da relação entre a temperatura do reator e o rendimento com Coeficiente de Pearson.

## Principais Insights Encontrados
- **Variação por Dia da Semana:** Identificou-se que os lotes produzidos aos domingos apresentam o menor rendimento médio da fábrica (~87,3%), contra mais de 93% no meio da semana, indicando possível impacto de troca de turno ou escalas reduzidas.
- **Temperatura vs. Rendimento:** A correlação calculada ficou próxima de zero (~0.07), indicando que a oscilação de temperatura observada nos reatores não é o fator linear causador da perda de rendimento.

## Próximos Passos
- Conexão da base tratada (`lotes_producao_tratados.csv`) com o Power BI.
- Modelagem dimensional e criação de medidas em DAX.