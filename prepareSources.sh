#!/bin/bash
# before this "sudo pip install IMDbPy"
# SQLite 3.7 or later is the fastest
# --sqlite-transactions - that is extremely important for speed
imdbpy2sql.py -d sources -u sqlite:./imdb_raw.db --sqlite-transactions
