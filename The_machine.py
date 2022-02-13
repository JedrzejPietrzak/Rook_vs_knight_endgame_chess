import numpy as np
import pandas as pd
from functions import replace_draws



# Creating the machine model

df = pd.read_csv('krkopt.data.csv').drop('index', axis=1)
df['won'] = df['draw'].apply(replace_draws)
wh_king_pos = pd.get_dummies(df['a']).rename(columns={'a':'wa','b':'wb','c':'wc','d':'wd'})
rook_pos = pd.get_dummies(df['b']).rename(columns={'a':'Wa','b':'Wb','c':'Wc','d':'Wd'})
blk_king_pos = pd.get_dummies(df['c'])
df.drop(['a', 'b', 'c'], axis=1, inplace=True)
df = pd.concat([df, wh_king_pos, rook_pos, blk_king_pos], axis=1)
df.drop('draw', axis=1, inplace=True)


# Training the model

from sklearn.model_selection import train_test_split
X = df.drop('won', axis=1)
y = df['won']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# creating an Knn instance

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(X_train, y_train) # We are not predicting any test data, since the model was already checked in ML_rook_vs_knight.ipynb