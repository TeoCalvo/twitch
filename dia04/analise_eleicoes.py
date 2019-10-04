import pandas as pd
import os

BASE_DIR = os.path.abspath(".")
DATA_DIR = os.path.join(BASE_DIR, "dia04")

df = pd.read_csv(os.path.join(DATA_DIR, "resumo_eleicoes.csv"))

df_bolsonaro = df.where(df["nome_urna"] == "JAIR BOLSONARO").dropna(how="all")
df_bolsonaro = df_bolsonaro.sort_values(by="total_votos")
columns = ['nome_urna', 'numero_turno', 'sigla_uf', 'total_votos']
df_bolsonaro[columns]


df_haddad = df.where(df["nome_urna"] == "FERNANDO HADDAD").dropna(how="all")
df_haddad = df_haddad.sort_values(by="total_votos")
columns = ['nome_urna', 'numero_turno', 'sigla_uf', 'total_votos']
print(df_haddad[columns])