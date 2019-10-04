import pandas as pd
import sqlalchemy
import os
import dotenv
import argparse

dotenv.load_dotenv( dotenv.find_dotenv() )

# DEFINE DIRETÓRIOS DO PROJETO
BASE_DIR = os.path.abspath('.')
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
SQL_DIR = os.path.join( BASE_DIR, 'sql'  )

def import_query( query_name ):
    '''Função para importar query com base no nome'''
    file_name = "{}.sql".format(query_name)
    with open( os.path.join( SQL_DIR, file_name), "r" ) as query_file:
        query = query_file.read()
    return query

# Abre conexão com o bacno
con_str = "sqlite:///{path}".format(path= os.getenv( "SQLITE_BRASIL_IO_HOST" )  )

# conexão para iniciante
# engine = sqlalchemy.create_engine( "sqlite:////home/teo/Documentos/pessoais/projetos/brasilIo/data/db/brasil_new.db" )
engine = sqlalchemy.create_engine(con_str)

# Bate no banco para saber quais são as racas possíveis
racas = pd.read_sql_query( import_query( "get_racas" ), engine )['RACA'].tolist()

# Parser para usuário selecionar a raca
parser = argparse.ArgumentParser()
parser.add_argument("--raca", help="Cor da pele", choices=racas, nargs='+' )
args = parser.parse_args()

racas_select = ",".join( [ "'{}'".format(i) for i in args.raca ] )

# Executa a contagem da raça por cargo
query = import_query("query_raca_cargo")

query = query.format( racas = racas_select )
df = pd.read_sql_query( query, engine )

df.to_sql( "TABELA_TESTE", engine, if_exists="replace" )