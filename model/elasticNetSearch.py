from CustomSQLFeatureExtractor import *
import numpy as np
import apsw
import datetime
from sklearn.pipeline import Pipeline
from sklearn.linear_model import ElasticNetCV
from sklearn.metrics import mean_squared_error
from sklearn.cross_validation import train_test_split

# get and split the data
homefolder = '.'
c = apsw.Connection(homefolder + '/imdb.sqlite').cursor()
all_data = c.execute('SELECT movie_id, rating FROM movies ORDER BY movie_id').fetchall()
train_data, test_data = train_test_split(all_data, train_size = 0.8, random_state = 17273)
train_data = np.asarray(sorted(train_data))
test_data = np.asarray(sorted(test_data))
X_train, y_train = train_data[:, 0], train_data[:, 1]
X_test, y_test = test_data[:, 0], test_data[:, 1]

# construct pipeline
featureExtractor = CustomSQLFeatureExtractor(homefolder + '/imdb.sqlite',\
    homefolder + '/transformData.sql', True)
elastic = ElasticNetCV(n_jobs = 1, cv = 10, l1_ratio = [.5, 1], n_alphas = 100, eps = 0.001)
clf = Pipeline([('FeatureExtractor', featureExtractor), ('ElasticNet', elastic)])

# fit the model
print(datetime.datetime.now())
clf.fit(X_train, y_train)
print(datetime.datetime.now())

# print results
mse = np.var([y for (x, y) in all_data])
print("Baseline MSE: %.4f" % mse)
mse = mean_squared_error(y_train, clf.predict(X_train))
print("Train MSE: %.4f" % mse)
mse = mean_squared_error(y_test, clf.predict(X_test))
print("Test MSE: %.4f" % mse)
print(elastic.l1_ratio_)
print(elastic.alpha_)
