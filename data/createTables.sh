#!/bin/bash
rm imdb.sqlite
sqlite3 < createTables.sql
