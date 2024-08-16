from datetime import datetime, timedelta

import numpy as np
import pandas as pd

# Configurações
np.random.seed(0)  # Para reprodutibilidade
num_rows = 300
start_date = datetime(2023, 1, 1)
date_range = [start_date + timedelta(days=i) for i in range(num_rows)]
categories = [
    "Marketing",
    "Salários",
    "Manutenção",
    "Suprimentos",
    "Serviços",
    "Outros",
]

# Gerar dados fictícios
data = {
    "Data": [date_range[i].strftime("%Y-%m-%d") for i in range(num_rows)],
    "Receita": np.random.uniform(1000, 5000, num_rows).round(2),
    "Despesas": np.random.uniform(500, 2000, num_rows).round(2),
    "Investimentos": np.random.uniform(100, 1000, num_rows).round(2),
}

# Calcular Lucro e Fluxo de Caixa
data["Lucro"] = (data["Receita"] - data["Despesas"]).round(2)
data["Fluxo de Caixa"] = (
    data["Receita"] - data["Despesas"] + data["Investimentos"].round(2)
)

# Adicionar categoria de despesas
data["Categoria de Despesa"] = np.random.choice(categories, num_rows)

# Calcular Desempenho Financeiro
data["Desempenho Financeiro"] = (data["Receita"] / (data["Despesas"] + 1)).round(
    2
)  # Adiciona 1 para evitar divisão por zero

# Criar DataFrame e salvar como CSV
df = pd.DataFrame(data)
df.to_csv("analise_financeira.csv", index=False)

print("Arquivo CSV 'analise_financeira.csv' criado com sucesso!")
print("Arquivo CSV 'analise_financeira.csv' criado com sucesso!")
