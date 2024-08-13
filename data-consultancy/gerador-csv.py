import random
from datetime import datetime, timedelta

import pandas as pd


# Função para gerar uma data aleatória dentro de um intervalo
def random_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))


# Configurações iniciais
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 6, 30)
n_records = 500

# Dados de exemplo
data = {
    "ID": range(1, n_records + 1),
    "Data": [
        random_date(start_date, end_date).strftime("%Y-%m-%d") for _ in range(n_records)
    ],
    "Produção (unidades)": [random.randint(130, 170) for _ in range(n_records)],
    "Tempo de Entrega (horas)": [
        round(random.uniform(20, 30), 2) for _ in range(n_records)
    ],
    "Custo Operacional ($)": [
        round(random.uniform(1100, 1300), 2) for _ in range(n_records)
    ],
    "Eficiência de Produção (%)": [
        round(random.uniform(65, 85), 2) for _ in range(n_records)
    ],
    "Unidades Planejadas": [200 for _ in range(n_records)],
    "Turnover de Funcionários (%)": [
        round(random.uniform(3, 7), 2) for _ in range(n_records)
    ],
    "Feedback dos Clientes (0-10)": [
        round(random.uniform(5, 9), 2) for _ in range(n_records)
    ],
}

df = pd.DataFrame(data)
df.to_csv("performance_data.csv", index=False)
df = pd.DataFrame(data)
df.to_csv("performance_data.csv", index=False)
