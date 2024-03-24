# BINARY LINEAR CLASSIFIER: SPACE DIVIDED BY 'STRAIGHT' HYPERPLANE, WHICH SEPARATES THE SPACE IN CATEGORY A AND CATEGORY B
# THE HYPERPLANE TO CHOOSE IS OFTEN THE ONE THAT MAXIMIZES THE MARGIN (DISTANCE TO DATA POINTS)
# THE POINTS THAT THE HYPERPLANE IS CLOSEST TO AND INFLUENCED BY TO MAXIMIZE ITS MARGIN, ARE CALLED SUPPORT VECTORS
# NON-LINEARLY SEPARABLE DATA SEPARATED BY KERNEL TRICK, WHICH IS NOT EXCLUSIVE TO SUPPORT VECTOR MACHINES, BUT MOST OFTEN USED THERE


import numpy
import pandas
import matplotlib
from matplotlib import pyplot
import seaborn

import sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.grid_search import GridSearchCV

cancer = load_breast_cancer()
print(cancer.keys())
# print("DATA IS: ",cancer["data"])
# print("TARGET IS: ",cancer["target"])
# print("TARGET NAMES IS: ",cancer["target_names"])
# print("DESCRIPTION IS: ",cancer["DESCR"])
# print("FEATURE NAMES IS: ",cancer["feature_names"])
cancer_dataframe = pandas.DataFrame(cancer["data"], columns = cancer['feature_names'])
cancer_dataframe.info()

X = cancer_dataframe
y = cancer["target"]
Xtr, Xts, ytr, yts = train_test_split(X, y, test_size = 0.33)

vector = SVC()
vector.fit(Xtr,ytr)
pred = vector.predict(Xts)

print(classification_report(yts, pred))
print(confusion_matrix(yts,pred))

# WHEN EXECUTING THIS WITH STANDARD PARAMETERS, EVERYTHING IS CLASSIFIED AS 1 
# TO INVESTIGATE DIFFERENT POSSIBLE COMBINATIONS OF PARAMETERS, EXECUTE GRIDSEARCH
# THE PARAMETERS TO VARY ARE GIVEN IN A DICTIONAIRY:
parameter_grid = {'C': [1e-1,1e0,1e1,1e2,1e3,1e4], 'gamma': [1e1,1e0,1e-1,1e-2,1e-3,1e-4]}
# AND PUT INTO THE GRIDSEARCH, WHICH FROM THAT MOMENT ON BEHAVES AS A NEW SKLEARN METHOD
grid = GridSearchCV(SVC(), parameter_grid)
grid.fit(Xtr,ytr)
# AFTER A FIT YOU CAN CHECK WHAT THE BEST PARAMETERS ARE:
print(grid.best_params_)
pred = grid.predict(Xts)

print(classification_report(yts, pred))
print(confusion_matrix(yts,pred))
