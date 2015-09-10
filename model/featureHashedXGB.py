import apsw
c = apsw.Connection("../data/imdb.sqlite")
movie_data = c.cursor().execute("select * from movie_data").fetchall()
c.close()
del c
del apsw

x = [x.split(',') for (x, y) in movie_data]
y = [y for (x, y) in movie_data]
del movie_data

from sklearn.feature_extraction import FeatureHasher
fh = FeatureHasher(input_type = "string")
X = fh.transform(x)
del x
del fh
del FeatureHasher

import xgboost as xgb
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer

xgbRegr = xgb.XGBRegressor()
clf = GridSearchCV(Pipeline([('XGBoost', xgbRegr)]),
    {'XGBoost__max_depth': [1], 'XGBoost__n_estimators': [20]}, verbose=1, n_jobs = -1,
    scoring = make_scorer(mean_squared_error, greater_is_better = False), cv = 3)
clf.fit(X, y)
print(clf.best_score_)
print(clf.best_params_)
print(clf.grid_scores_)