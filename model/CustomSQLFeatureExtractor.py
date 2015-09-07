import numpy
import apsw
from sklearn.base import BaseEstimator

class CustomSQLFeatureExtractor(BaseEstimator):
    def __init__(self, dbfile, queryfile):
        self.dbfile = dbfile
        self.queryfile = queryfile
        # read text of query from disk into memory
        self.query = open(self.queryfile, "r").read()

    # dummy method - only for pipeline compatibility
    def fit(self, X, y):
        return self

    def transform(self, X):
        # create an inmemory DB - needed for parallel computations
        conn = apsw.Connection(":memory:")
        # copy DB from disk into memory
        conn.backup("main", apsw.Connection(self.dbfile), "main").step()
        c = conn.cursor()
        # prepare input
        c.execute("delete from train_ids")
        c.executemany("INSERT INTO train_ids (movie_id) VALUES (?)", [(x,) for x in X.tolist()])
        # execute main transformation and load the result
        c.execute(self.query)
        X = numpy.asarray(c.execute("""
            SELECT actor, producer, writer,
            cinematographer, composer, costume_director,
            director, editor, misc, production_designer FROM train_data ORDER BY movie_id
        """).fetchall())
        # destroy inmemory snapshot and return the result
        conn.close()
        return X