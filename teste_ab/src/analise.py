import pandas as pd
import os

SRC_DIR = os.path.join( os.path.abspath("."), 'src' ) # Onde o python está referente aos diretórios do PC
BASE_DIR = os.path.dirname(SRC_DIR) # Define o caminho raiz do projeto
DATA_DIR = os.path.join(BASE_DIR, 'data') # Define caminho do diretório de dados

df = pd.read_excel(os.path.join(DATA_DIR, 'dados.xlsx')) # Lê o arquivo de dados

# Define variáveis categóricas
cat_vars = ['Já conhecia/conhece nossas lives?',
            'Quantas vezes participou?',
            'Já compartilhou meu conteúdo com amigos?']


num_vars = ['Nota que você daria para nossa iniciativa?',
            'Qual a sua idade? (em anos e apenas números)']

# Cria dummies para análise
df_dummy = pd.get_dummies( df[cat_vars] )
dummy_cols = df_dummy.columns.tolist()

# Cria df com variáveis dummies a originais
df_full = pd.concat( [df,df_dummy], axis=1)

# Realiza o profile de cada canal (teste A, B, C....)
df_analise_cat = df_full.groupby( 'Canal que recebeu esse link' )[dummy_cols].mean()
df_analise_cat.to_excel( os.path.join(DATA_DIR, "analise_cat.xlsx") )

# Realiza o profile de cada canal (teste A, B, C....)
df_analise_num = df_full.groupby( 'Canal que recebeu esse link' )[num_vars].mean()
df_analise_num.to_excel( os.path.join(DATA_DIR, "analise_num.xlsx") )
