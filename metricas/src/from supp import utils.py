from supp import utils
import pandas as pd
import numpy as np

import time

from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import model_selection
from sklearn import metrics

import xgboost as xgb

from hero.models import Tan_Gauss

# Conecta e pega a base do banco...

print("\n Extraindo ABT....")
con = utils.connect_mariadb()
df = pd.read_sql_table( 'ABT_DRAFT',  con, schema='dotadb' )
print(" Ok.")

print(f"\n\n A base tem {df.shape[0]} linhas")

# Define as variáveis resposta e features para o treinamento
target = 'radiant_win'
features = [i for i in df.columns if 'hero' in i]
features = features[: features.index('dire_hero_129')+1 ]

# Split da base
print("\n Separando base de treino e de teste...")
X_train, X_test, y_train, y_test = model_selection.train_test_split( df[features],
                                                                     df[target],
                                                                     train_size=0.9,
                                                                     random_state=1992)
print(" Ok.")

print("\n Treinando algoritmos...")
# Treinando o Naive-Bayes
clf_nb = BernoulliNB()
clf_nb.fit( X_train, y_train )

# Treinando um modelo de arvore de decisão
clf_tree = DecisionTreeClassifier(min_samples_leaf=5)
clf_tree.fit( X_train, y_train )

# Calcular a probabilidade de cada classe para Naive Bayes
nb_prob_train = clf_nb.predict_proba( X_train )
nb_pred_train = clf_nb.predict(X_train)

acc_nb = metrics.accuracy_score( y_train, nb_pred_train ) # Acurácia para Naive bayes
precision_nb = metrics.precision_score( y_train, nb_pred_train ) # Precision para Naive Bayes
recall_nb = metrics.recall_score( y_train, nb_pred_train ) # Recall para Naive Bayes
print("Métricas de ajuste NB:", acc_nb, precision_nb, recall_nb )

# Calcular a probabilidade de cada classe para arvore de decisao
tree_prob_train = clf_tree.predict_proba( X_train )
tree_pred_train = clf_tree.predict( X_train )

acc_tree = metrics.accuracy_score( y_train, tree_pred_train ) # Acurácia para Naive bayes
precision_tree = metrics.precision_score( y_train, tree_pred_train ) # Precision para Naive Bayes
recall_tree = metrics.recall_score( y_train, tree_pred_train ) # Recall para Naive Bayes
print("Métricas de ajuste Tree:", acc_tree, precision_tree, recall_tree)

# Testando agora na base de Teste!!
# Calcular a probabilidade de cada classe para Naive Bayes
nb_prob_test = clf_nb.predict_proba( X_test )
nb_pred_test = clf_nb.predict(X_test)

acc_nb = metrics.accuracy_score( y_test, nb_pred_test ) # Acurácia para Naive bayes
precision_nb = metrics.precision_score( y_test, nb_pred_test ) # Precision para Naive Bayes
recall_nb = metrics.recall_score( y_test, nb_pred_test ) # Recall para Naive Bayes
auc_nb = metrics.roc_auc_score( y_test, nb_prob_test[:,1] )
print("Métricas de ajuste NB:", acc_nb, precision_nb, recall_nb, auc_nb )

# Calcular a probabilidade de cada classe para arvore de decisao
tree_prob_test = clf_tree.predict_proba( X_test )
tree_pred_test = clf_tree.predict( X_test )

acc_tree = metrics.accuracy_score( y_test, tree_pred_test ) # Acurácia para Naive bayes
precision_tree = metrics.precision_score( y_test, tree_pred_test ) # Precision para Naive Bayes
recall_tree = metrics.recall_score( y_test, tree_pred_test ) # Recall para Naive Bayes
auc_tree = metrics.roc_auc_score(y_test, tree_prob_test[:,1] )
print("Métricas de ajuste Tree:", acc_tree, precision_tree, recall_tree, auc_tree)

import matplotlib.pyplot as plt

tree_roc = metrics.roc_curve( y_test, tree_prob_test[:,1] )
nb_roc = metrics.roc_curve( y_test, nb_prob_test[:,1] )

plt.plot( tree_roc[0], tree_roc[1] )
plt.plot( nb_roc[0], nb_roc[1] )
plt.legend( ['Arvore', "NaiveBayes"] )
plt.title("Curva ROC")
plt.xlabel("1 - Especificidade")
plt.ylabel("Sensibilidade")
plt.grid(True)
plt.show()