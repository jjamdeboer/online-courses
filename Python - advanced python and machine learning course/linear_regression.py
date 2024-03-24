import pandas
import numpy
import matplotlib
import seaborn
from matplotlib import pyplot

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn import metrics

durk = pandas.read_csv('USA_Housing.csv')
print(durk.head())
durk.info()
print(durk.describe())
print("\n\n\n\n")

# EXPLORE THE DATA HOW YOU SEE FIT:
# seaborn.pairplot(durk)
# pyplot.show()
# seaborn.distplot(durk["Price"])
# pyplot.show()
# seaborn.heatmap(durk.corr(),cmap = 'coolwarm')
# pyplot.show()

# VARIABLES/FEATURES:
X = durk[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']]
# THE TO BE PREDICTED VARIABLE:
y = durk["Price"]

# SPLIT DATA IN TEST AND TRAIN PART:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)

# MAKE A LINEAR MODEL AND FIT IT TO THE DATA:
lin = LinearRegression()
lin.fit(X_train, y_train)
# THE INTERCEPT AND THE COEFFICIENTS:
print(lin.intercept_, lin.coef_)
# FOR NICER OVERVIEW, MAKE NEW DATAFRAME CONTAINING BOTH:
durkudurk = pandas.DataFrame(lin.coef_,X_train.columns,columns = ["Coefficients"])
print(durkudurk)
print("\n\n\n\n")

# FOR PREDICTIONS:
pred = lin.predict(X_test)
# HOW FAR ARE THE PREDICTIONS FROM THE REAL DATA:
durkudurkudurk = pandas.DataFrame(pred,X_test.index)
durkudurkudurk = pandas.concat([durkudurkudurk,y_test], axis = 1)
durkudurkudurk.columns = ["Prediction", "Original data"]
seaborn.lmplot(x = "Prediction",y = "Original data", data  = durkudurkudurk)
pyplot.show()
# WHEN RESIDUALS NORMALLY DISTRIBUTED, IT'S A GOOD SIGN:
seaborn.histplot(y_test-pred, kde = True)
pyplot.show()

# MINIMIZE THE FOLLOWING FUNCTIONS:
# ABSOLUTE ERROR:
print("MAE: ", metrics.mean_absolute_error(y_test,pred))
# MEAN SQUARE ERROR (SQUARE THESE ERRORS):
print("MSE: ", mse := metrics.mean_squared_error(y_test,pred))
# TAKE ROOT SQUARE OF PREVIOUS RESULT:
print("RMSE: ", numpy.sqrt( mse ))
