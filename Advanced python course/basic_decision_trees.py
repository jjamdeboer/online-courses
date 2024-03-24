# NODES: THERE A SPLIT TAKES PLACE BETWEEN MULTIPLE ALTERNATIVES
# EDGES: OUTCOME OF SPLIT TO NEXT MODES
# ROOT: FIRST NODE
# LEAVES: FINAL EDGES

import pandas
import numpy
import matplotlib
from matplotlib import pyplot
import seaborn
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

kyphosis = pandas.read_csv("kyphosis.csv")
kyphosis.info()

seaborn.pairplot(kyphosis,hue = "Kyphosis")
pyplot.show()

X = kyphosis.drop("Kyphosis", axis = 1)
y = kyphosis["Kyphosis"]

# DECISION TREE:
Xtr, Xts, ytr, yts = train_test_split(X,y,test_size = 0.33)

tree = DecisionTreeClassifier()
tree.fit(Xtr,ytr)
pred = tree.predict(Xts)

print(confusion_matrix(yts,pred))
print(classification_report(yts,pred))

# RANDOM TREE:
Xtr, Xts, ytr, yts = train_test_split(X,y,test_size = 0.33)

forest = RandomForestClassifier(n_estimators = 200)
forest.fit(Xtr,ytr)
pred = forest.predict(Xts)

print(confusion_matrix(yts,pred))
print(classification_report(yts,pred))
