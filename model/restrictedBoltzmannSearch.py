import apsw
c = apsw.Connection("../data/imdb.sqlite")
movie_data = c.cursor().execute("select * from movie_data").fetchall()
c.close()
del c
del apsw

X = [x.split(',') for (x, y) in movie_data]
y = [y for (x, y) in movie_data]
del movie_data

from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
from sklearn.feature_extraction import FeatureHasher
from sklearn.neural_network import BernoulliRBM
thePipe = Pipeline([
    ("hash", FeatureHasher(input_type = "string")),
    ('RBM', BernoulliRBM()),
    ('XGB', XGBRegressor())
])

from sklearn.grid_search import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer

paramGrid = {
    'XGB__max_depth': [3],
    'XGB__n_estimators': [100],
    'RBM__n_components': [20],
    "hash__n_features": [100000]
}

theScorer = make_scorer(mean_squared_error, greater_is_better = False)

clf = GridSearchCV(
    thePipe,
    paramGrid,
    verbose = 2,
    n_jobs = -1,
    scoring = theScorer,
    cv = 3
)

clf.fit(X, y)
print(clf.best_score_)
print(clf.best_params_)
print(clf.grid_scores_)