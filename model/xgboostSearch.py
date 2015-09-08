import xgboost as xgb
import numpy as np
from sklearn.grid_search import GridSearchCV
from CustomSQLFeatureExtractor import *
import numpy as np
import apsw
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, make_scorer, mean_absolute_error, median_absolute_error
from sklearn.cross_validation import train_test_split

# get and split the data
rng = np.random.RandomState(31337)
homefolder = '../data'
# read text of query from disk into memory
query = open(homefolder + '/transformData.sql', "r").read()
c = apsw.Connection(homefolder + '/imdb.sqlite').cursor()
all_data = c.execute('SELECT movie_id, rating FROM movies ORDER BY movie_id').fetchall()
train_data, test_data = train_test_split(all_data, train_size = 0.6, random_state = rng)
train_data = np.asarray(sorted(train_data))
test_data = np.asarray(sorted(test_data))
X_train, y_train = train_data[:, 0], train_data[:, 1]
X_test, y_test = test_data[:, 0], test_data[:, 1]

# construct pipeline
featureExtractor = CustomSQLFeatureExtractor(query)
xgbRegr = xgb.XGBRegressor()
clf = GridSearchCV(Pipeline([('FeatureExtractor', featureExtractor), ('XGBoost', xgbRegr)]),
    {'XGBoost__max_depth': [8], 'XGBoost__n_estimators': [130]}, verbose=1, n_jobs = -1,
    scoring = make_scorer(mean_squared_error, greater_is_better = False), cv = 3)

# fit the model
clf.fit(X_train, y_train)
print(clf.best_score_)
print(clf.best_params_)
print(clf.grid_scores_)

# print results
r = [y for (x, y) in all_data]
a = np.mean(r)
r0 = [np.abs(x-a) for x in r]
mse = np.var(r)
mae = np.mean(r0)
medae = np.median(r0)
print("Baseline RMSE: %.4f" % np.sqrt(mse))
print("Baseline mean absolute error: %.4f" % mae)
print("Baseline median absolute error: %.4f" % medae)
mse = mean_squared_error(y_train, clf.predict(X_train))
print("Train MSE: %.4f" % mse)
pred = clf.predict(X_test)
mse = mean_squared_error(y_test, pred)
mae = mean_absolute_error(y_test, pred)
medae = median_absolute_error(y_test, pred)
print("Test RMSE: %.4f" % np.sqrt(mse))
print("Test mean absolute error: %.4f" % mae)
print("Test median absolute error: %.4f" % medae)
