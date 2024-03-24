# TRUE POSITIVES = PREDICTED POSITVE, ACTUALLY POSITIVE
# TRUE NEGATIVES = PREDICTED NEGATIVE, ACTUALLY NEGATIVE
# FALSE POSITIVES = PREDICTED POSITIVE, ACTUALLY NEGATIVE; TYPE 1 ERROR
# FALSE NEGATIVES = PREDICTED NEGATIVE, ACTUALLY POSITIVE; TYPE 2 ERROR
# ACCURACY = (TRUE POSITVES + TRUE NEGATIVES)/ SAMPLE SIZE
# MISCLASSIFICATION = 1 - ACCURACY = (FALSE POSITIVES + FALSE NEGATIVES)/SAMPLE SIZE

import pandas
import numpy
import matplotlib
from matplotlib import pyplot
import seaborn
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix

train = pandas.read_csv("titanic_train.csv")
train.info()
# print(train.head())

#  THIS IS FOR EXPLORATORY ANALYSES TO CHECK WHAT COLUMNS HAVE MISSING VALUES
# seaborn.heatmap(train.isnull(),yticklabels = False, cbar = False, cmap = 'magma')
# pyplot.show()

# seaborn.countplot(x = 'Survived', data = train, hue = 'Sex', palette = 'RdBu_r')
# pyplot.show()

# seaborn.histplot(train["Age"].dropna(),kde=False)
# pyplot.show()

# REPLACE AGE BY AGE IN PCLASS:
for x in 1,2,3:
    train.loc[train["Pclass"] == x, "Age"] = train.loc[train["Pclass"] == x, "Age"].fillna(train.loc[train["Pclass"] == x, "Age"].mean())
train.drop(["PassengerId", "Cabin"], axis = 1, inplace = True)
train["Embarked"].fillna(train["Embarked"].value_counts().index[0], inplace = True)

# ADD DUMMY VARIABLE FOR SEX AND EMBARKED:
#  SINCE CREATING TWO COLUMNS (IT CREATES A COLUMN FOR BOTH MALE AND FEMALE) BOTH COLUMNS ARE PERFECTLY ANTI-CORRELATED
#  BECAUSE OF THIS, THE FIRST ONE NEEDS TO BE DROPPED
#  NOTE THAT THE DUMMIES EXPLICITLY NEEDS TO BE CONVERTED TO NUMERICALS, OTHERWISE IT WOULD BE IGNORED VIA THE DESCRIBE-METHOD
train["Sex dummy"] = pandas.get_dummies(train['Sex'], drop_first = True).astype( int )
train[["Embarked dummy one", "Embarked dummy two"]] = pandas.get_dummies(train['Embarked'], drop_first = True).astype( int )

train = train[train.describe().columns]
train.info()

y = train["Survived"]
X = train.drop("Survived",axis = 1)

Xtr, Xts, ytr, yts = train_test_split(X, y, test_size = 0.33)

#  MAXIMUM NUMBER OF ITERATION NEEDED TO BE INCREASED FOR CONVERGENCE
lmod = LogisticRegression( max_iter = 250 )
lmod.fit(Xtr, ytr)
pred = lmod.predict(Xts)

print(classification_report(yts, pred))
print(confusion_matrix(yts,pred))