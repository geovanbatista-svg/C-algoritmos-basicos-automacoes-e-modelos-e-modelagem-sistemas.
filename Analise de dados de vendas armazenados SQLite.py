# ===============================================
# Passo 1: Conectar ao banco de dados e inserir dados
# ===============================================

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Conectar (ou criar) o banco de dados
conexao = sqlite3.connect('dados_vendas.db')
cursor = conexao.cursor()

# Criar tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')

# Inserir dados fictícios (se ainda não existir nada)
cursor.execute("DELETE FROM vendas1")  # limpa a tabela antes de inserir de novo
cursor.execute('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES  
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00), 
    ('2023-01-05', 'Produto B', 'Roupas', 350.00), 
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00), 
    ('2023-03-15', 'Produto D', 'Livros', 200.00), 
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00), 
    ('2023-04-02', 'Produto F', 'Roupas', 400.00), 
    ('2023-05-05', 'Produto G', 'Livros', 150.00), 
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00), 
    ('2023-07-20', 'Produto I', 'Roupas', 600.00), 
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00), 
    ('2023-09-30', 'Produto K', 'Livros', 300.00), 
    ('2023-10-05', 'Produto L', 'Roupas', 450.00), 
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00), 
    ('2023-12-20', 'Produto N', 'Livros', 250.00);
''')

conexao.commit()

# ===============================================
# Passo 2: Explorar e preparar os dados
# ===============================================

df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)

# Converter a coluna de datas para tipo datetime
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])

print("Visualização inicial dos dados:")
print(df_vendas.head())

# ===============================================
# Passo 3: Análise dos dados
# ===============================================

# Vendas totais
print("\nValor total de vendas:", df_vendas['valor_venda'].sum())

# Vendas por categoria
print("\nVendas por categoria:")
print(df_vendas.groupby('categoria')['valor_venda'].sum())

# Média de vendas por mês
df_vendas['mes'] = df_vendas['data_venda'].dt.month
print("\nMédia de vendas por mês:")
print(df_vendas.groupby('mes')['valor_venda'].mean())

# ===============================================
# Passo 4: Visualização dos dados
# ===============================================

plt.figure(figsize=(10,5))
sns.barplot(x='categoria', y='valor_venda', data=df_vendas, estimator=sum, ci=None)
plt.title("Total de Vendas por Categoria") 
plt.ylabel("Valor Total (R$)")
plt.show()

plt.figure(figsize=(12,6))
df_vendas.groupby('mes')['valor_venda'].sum().plot(kind='line', marker='o')
plt.title("Vendas ao longo dos meses de 2023")
plt.xlabel("Mês")
plt.ylabel("Valor Total (R$)")
plt.show()

# ===============================================
# Passo 5: Conclusão e insights
# ===============================================

print("INSIGHTS:")
print("- A categoria 'Eletrônicos' lidera as vendas, com valores bem acima das demais.")
print("- O segundo setor com destaque foi 'Roupas'.")
print("- 'Livros' tem faturamento baixo, mas vendas constantes durante o ano.")
print("- A empresa pode investir em promoções de eletrônicos em meses de menor venda e")
print("  explorar melhor o segmento de livros com campanhas de fidelização.")