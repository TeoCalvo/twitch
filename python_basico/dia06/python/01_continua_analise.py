import pandas as pd

df = pd.read_csv( "dia05/dados_candidatos.csv", sep=";", decimal="," )

# Ver 5 primeiras linhas
df.head()

# Ver o final da tabela (dataframe)
df.tail()

# Mostrar colunas
df.columns

# Tamanho do dataframe
df.shape

# summary - Descritiva do dataframe
df.describe()

# Tabela de frequencia univariado
pd.value_counts( df["nome_partido"] )

# Tabela de frequencia relativa
pd.value_counts( df["nome_partido"] ) / df["nome_partido"].count()

# Tabela cruzada (bivariada)
tb = pd.crosstab( df["descricao_genero"], df["descricao_cor_raca"] )

# Aprendendo groupby
df.groupby( ["sigla_uf_nascimento"] )["patrimonio"].mean()
df.groupby( ["sigla_uf_nascimento"] )["patrimonio"].sum()

tb_agregada_estado = df.groupby( ["sigla_uf_nascimento"] ).agg( { "patrimonio": ['sum', 'mean'] } )
tb_agregada_estado.round(0)

# Aplicando funções em uma serie (coluna do dataframe)
def format_estado_civel( x ):
    x = x.lower().replace("(a)", "")
    x = x[0].upper() + x[1:]
    return x

# Sem usar lambda
estado_civil = df["descricao_estado_civil"].apply( format_estado_civel )

# Usando lambda
estado_civil = df["descricao_estado_civil"].apply( lambda x: x[0] + x[1:].lower().replace("(a)","") )
