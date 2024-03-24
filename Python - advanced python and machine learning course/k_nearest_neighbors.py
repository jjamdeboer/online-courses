import pandas
import numpy
import matplotlib
import seaborn
from matplotlib import pyplot

import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

durk = pandas.read_csv("Classified Data", index_col = 0)
durk.info()
print(durk.describe())

#  NOTE HOW MUCH THIS LOOKS TO FITTING A NORMAL MODEL
scaler = StandardScaler()
scaler.fit(durk.drop("TARGET CLASS", axis = 1))
scale_two = scaler.transform(durk.drop("TARGET CLASS", axis = 1))

# MAKE A NEW DATAFRAME, HAVING EVERYTHING BUT THE TARGET FEATURE:
durkudurk = pandas.DataFrame(scale_two,columns = durk.columns[:-1])
durkudurk.info()
print(durkudurk.head())

y = durk["TARGET CLASS"]
X = durkudurk

Xtr, Xts, ytr, yts = train_test_split(X, y, test_size = 0.33)

knn = KNeighborsClassifier(n_neighbors = 25)
knn.fit(Xtr, ytr)
pred = knn.predict(Xts)

print(classification_report(yts, pred))
print(confusion_matrix(yts,pred))

# TO OPTIMIZE K, USE FOR-LOOP:
error_rate =[]
for i in range(1,300):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(Xtr, ytr)
    pred = knn.predict(Xts)
    error_rate.append(numpy.mean(pred != yts))

canvas = pyplot.figure()
#  CREATES AXES AS PERCENTAGE OF RANGE OF X AND Y (XMIN, YMIN, X-SCALE, Y-SCALE)
axes = canvas.add_axes([ .15, .15, .8, .8 ])
axes.plot( error_rate, label = 'Elbow', color = 'r', linewidth = 5, alpha = 0.2, linestyle = '--', marker = 'o', markersize = 2)
#  axes = pyplot.gca()
#  axes.set_xlim([10,150])
#  axes.set_ylim([-1e9,1e9])
axes.set_xlabel("K")
axes.set_ylabel("Error Rate")
axes.set_title("KNN")
axes.legend()
   
pyplot.show()
print(min(error_rate), error_rate.index(min(error_rate)))
