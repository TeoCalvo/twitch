import pandas as pd
from sklearn import tree
from sklearn import preprocessing
from sklearn import metrics

from sklearn.externals import joblib

# Importa a base de dados
df = pd.read_csv( 'data/celulas.csv', sep=";" )

# Define quem é a variável resposta
target = 'classe'

# Define quais são as features/variáveis regressortas
features_num = ['nucleos','caudas']
features_cat = ['cor','membrana']

# Cria encoder de dados categóricos para numéricos
onehot = preprocessing.OneHotEncoder(sparse=False)  # Cria um objeto de onehot encoder
onehot.fit( df[features_cat] ) # Treina os tipos de variáveis categóricas para numérico
new_columns = onehot.get_feature_names(features_cat) # Definie novo nome das colunas com cada categoria
df_cat = pd.DataFrame( onehot.transform( df[features_cat] ), columns=new_columns ) # Cria dataframe com os valores numéricos
df_treino = pd.concat( [ df[features_num] , df_cat ], axis=1  )

# Cria a arvore de decisao sem criterio de parada
clf_tree = tree.DecisionTreeClassifier()

# Treina a arvore de decisao com os dados importados
clf_tree.fit( df_treino , df[target] )

# Fazendo predições
y_pred = clf_tree.predict( df_treino )

# Avaliando ajuste
metrics.accuracy_score( df[target] , y_pred )

# Prevendo a probabilidade
y_prob = clf_tree.predict_proba( df_treino )

# Salvando onehot encoder
joblib.dump( onehot, 'models/onehot.pkl' )

# Salvando arvore treinada
joblib.dump( clf_tree, 'models/tree.pkl' )