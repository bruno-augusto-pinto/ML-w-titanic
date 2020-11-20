import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df_train = pd.read_csv('Data/train.csv')
df_test = pd.read_csv('Data/test.csv')

entradas = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
saida = ['Survived']

x_train = df_train[entradas]
y_train = df_train[saida]
