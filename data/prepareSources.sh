#!/bin/bash
# before this "sudo pip install IMDbPy"
# SQLite 3.7 or later is the fastest
# --sqlite-transactions - that is extremely important for speed
# 2GB RAM needed
imdbpy2sql.py -d sources -u sqlite:./imdb_raw.sqlite --sqlite-transactions
