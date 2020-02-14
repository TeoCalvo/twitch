import pandas as pd
import joblib

# Importa os algoritmos treinados
onehot = joblib.load( 'models/onehot.pkl' )
clf_tree = joblib.load( 'models/tree.pkl' )

# Pega valores de input para realizar a predição da célula
caudas = int( input("Entre com o número de caudas da célula: ") )
nucleos = int( input("Entre com o número de nucleos da célula: ") )
cor = input("Entre com a cor Clara ou Escura da célula: ")
membrana = input("Entre com a membrana Grossa ou Fina da célula: ")

# Controi o dataframe para predição
data = { 'nucleos': [nucleos],
         'caudas': [caudas],
         'cor': [cor],
         'membrana': [membrana] }

data = pd.DataFrame( data )

# Define as variáveis preditoras
features_num = ['nucleos','caudas']
features_cat = ['cor','membrana']

# Aplica o onehot encode nas variáveis
data_cat = onehot.transform( data[features_cat] )
data_cat = pd.DataFrame( data_cat, columns=onehot.get_feature_names(features_cat) )
data_predict = pd.concat( [data[features_num], data_cat], axis=1)

# Realiza a predição
y_pred = clf_tree.predict( data_predict )

# Exibe o resultado da predição
print("A sua célula e do tipo:", y_pred[0])