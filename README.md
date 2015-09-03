# IMDB Rating Prediction

## General Info

* Data source: http://www.imdb.com/interfaces
* Data extraction: http://imdbpy.sourceforge.net/
* Data storage: SQLite 3.8
* Data transformation: SQL
* Modelling framework: scikit-learn (Python 3.4)

## Algorithms

* Minial votes: 1000
* Number of movies: 30459
* Baseline (mean rating) MSE: 1.8081

### ElasticNet

Optimal L1-ratio was found to be equal to 1 so model turn out to be a pure Lasso.

I used 10-fold cross-validation on a training set (80% of input data). 20% of input dat formed test set for final model estimation.

* MSE on training set 1.5912
* MSE on testing set: 1.6995

### XGBoost

Optimal model had 800 estimators with maximal depth of intercation being equal to 10.

I used 3-fold cross-validation on a training set (80% of input data). 20% of input dat formed test set for final model estimation.

* MSE on training set 0.0110
* MSE on testing set: 0.5748
