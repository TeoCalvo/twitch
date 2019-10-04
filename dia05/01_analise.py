import pandas as pd

# importar base de dados
df = pd.read_csv("dia05/dados_candidatos.csv", sep=";", decimal=",")

# exibir as primeiras linhas de dados
print(df.head())

# exibir as ultimas 5 linhas
print(df.tail())

# Quantas linhas esse dataframe tem?
print(df.shape)

# Quais são os tipos de colunas?
print(df.dtypes)

# Quais são as colunas?
print(df.columns)

# Procurando o Jairzin
jair = df[df["nome_urna"] == "JAIR BOLSONARO"]

# Só deputados
df_federais = df[df["descricao_cargo"] == 'DEPUTADO FEDERAL'].copy()

# Quantos deputados federais temos?
print(df_federais.shape[0])

# Qual o candidato mais votado no brasil?
print(df_federais[df_federais["total_votos_brasil"] == df_federais["total_votos_brasil"].max()]["nome_urna"])

# Reordena o dataframe com base em uma coluna
df_federais = df_federais.sort_values(by=["total_votos_brasil", "nome_urna"], ascending=False)

# Resetando indices depois da ordenação
df_federais = df_federais.reset_index(drop=True)
df_federais["total_votos_brasil"][0] - df_federais["total_votos_brasil"][1]

# Candidatos com mais de 100k votos
df_federais_100 = df_federais[df_federais["total_votos_brasil"] >= 100000]
group = df_federais_100.groupby("sigla_partido")
group["numero_sequencial"].count().sort_values()

# Quantidade de candidados por cor de pele
tb_freq_raca = df_federais.groupby("descricao_cor_raca")["numero_sequencial"].count().sort_values(ascending=False)
tb_freq_raca / tb_freq_raca.sum()

# Votos separados por genero e raca
df_federais.groupby(by=["descricao_genero", "descricao_cor_raca"])["total_votos_brasil"].sum()

# Quem ganhou em são paulo?
df_federais[df_federais["share_eleicao_SP"] == df_federais["share_eleicao_SP"].max()]["nome_urna"]
