from CustomSQLFeatureExtractor import *
import numpy as np
import apsw
import datetime
from sklearn.pipeline import Pipeline
from sklearn.linear_model import ElasticNetCV
from sklearn.metrics import mean_squared_error

# train and test data
homefolder = '.'
c = apsw.Connection(homefolder + '/imdb.sqlite').cursor()
train_data = np.asarray(c.execute(\
    'SELECT movie_id, rating FROM movies ORDER BY movie_id LIMIT 5000'\
).fetchall())
X_train, y_train = train_data[:, 0], train_data[:, 1]
test_data = np.asarray(c.execute(\
    'SELECT movie_id, rating FROM movies ORDER BY movie_id DESC LIMIT 1800'\
).fetchall())
X_test, y_test = test_data[:, 0], test_data[:, 1]

# our pipeline
featureExtractor = CustomSQLFeatureExtractor(homefolder + '/imdb.sqlite',\
    homefolder + '/transformData.sql', True)
elastic = ElasticNetCV(n_jobs=-1, cv=10)
clf = Pipeline([('FeatureExtractor', featureExtractor), ('ElasticNet', elastic)])

# fitting the model
print(datetime.datetime.now())
clf.fit(X_train, y_train)
print(datetime.datetime.now())

# printing the results
mse = mean_squared_error(y_train, clf.predict(X_train))
print("Train MSE: %.4f" % mse)
mse = mean_squared_error(y_test, clf.predict(X_test))
print("Test MSE: %.4f" % mse)
