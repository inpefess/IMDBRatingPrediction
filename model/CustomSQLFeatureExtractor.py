import numpy as np
import apsw
from sklearn.base import BaseEstimator

class CustomSQLFeatureExtractor(BaseEstimator):
    def __init__(self, dbfile, queryfile, inmemory, max_depth = 1, n_estimators = 50):
        self.dbfile = dbfile
        self.queryfile = queryfile
        self.inmemory = inmemory
        self.max_depth = max_depth
        self.n_estimators = n_estimators
        diskcon = apsw.Connection(dbfile)
        if inmemory:
            self.conn = apsw.Connection(":memory:")
            self.conn.backup("main", diskcon, "main").step()
        else:
            self.conn = diskcon
    
    def fit(self, X, y):
        return self

    def transform(self, X):
        c = self.conn.cursor()
        c.execute("delete from train_ids")
        c.executemany("INSERT INTO train_ids (movie_id) VALUES (?)", [(x,) for x in X.tolist()])
        c.execute(open(self.queryfile, "r").read())
        X = np.asarray(c.execute("""
            SELECT actor, producer, writer,
            cinematographer, composer, costume_director,
            director, editor, misc, production_designer FROM train_data ORDER BY movie_id
        """).fetchall())
        return X