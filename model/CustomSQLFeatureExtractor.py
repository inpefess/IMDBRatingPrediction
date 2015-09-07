import numpy
import apsw
from sklearn.base import BaseEstimator

class CustomSQLFeatureExtractor(BaseEstimator):
    def __init__(self, query):
        self.query = query

    # dummy method - only for pipeline compatibility
    def fit(self, X, y):
        return self

    def transform(self, X):
        # create an inmemory DB - needed for parallel computations
        conn = apsw.Connection(":memory:")
        c = conn.cursor()
        # prepare input
        c.execute("CREATE TABLE train_ids (movie_id INTEGER)")
        c.executemany("INSERT INTO train_ids (movie_id) VALUES (?)", [(x,) for x in X.tolist()])
        # execute main transformation and load the result
        c.execute(self.query)
        X = numpy.asarray(c.execute("SELECT * FROM train_data").fetchall())
        # destroy inmemory snapshot and return the result
        conn.close()
        return X
