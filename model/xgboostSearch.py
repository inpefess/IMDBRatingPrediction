import xgboost as xgb
import numpy as np
from sklearn.cross_validation import KFold, train_test_split
from sklearn.metrics import confusion_matrix, mean_squared_error
from sklearn.grid_search import GridSearchCV
from CustomSQLFeatureExtractor import *
import numpy as np
import apsw
import datetime
from sklearn.pipeline import Pipeline
from sklearn.linear_model import ElasticNetCV
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.cross_validation import train_test_split

# get and split the data
rng = np.random.RandomState(31337)
homefolder = '.'
dbfile = homefolder + '/imdb.sqlite'
c = apsw.Connection(dbfile).cursor()
all_data = c.execute('SELECT movie_id, rating FROM movies ORDER BY movie_id').fetchall()
train_data, test_data = train_test_split(all_data, train_size = 0.8, random_state = rng)
train_data = np.asarray(sorted(train_data))
test_data = np.asarray(sorted(test_data))
X_train, y_train = train_data[:, 0], train_data[:, 1]
X_test, y_test = test_data[:, 0], test_data[:, 1]

# construct pipeline
featureExtractor = CustomSQLFeatureExtractor(dbfile, homefolder + '/transformData.sql', True)
xgbRegr = xgb.XGBRegressor()
clf = GridSearchCV(Pipeline([('FeatureExtractor', featureExtractor), ('XGBoost', xgbRegr)]),
    {'XGBoost__max_depth': [1], 'XGBoost__n_estimators': [50, 100, 200, 400, 800]}, verbose=1,
    scoring = make_scorer(mean_squared_error))

# fit the model
clf.fit(X_train, y_train)
print(clf.best_score_)
print(clf.best_params_)

# print results
mse = np.var([y for (x, y) in all_data])
print("Baseline MSE: %.4f" % mse)
mse = mean_squared_error(y_train, clf.predict(X_train))
print("Train MSE: %.4f" % mse)
mse = mean_squared_error(y_test, clf.predict(X_test))
print("Test MSE: %.4f" % mse)
