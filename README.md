# IMDB Rating Prediction

## General Info

* Data source: http://www.imdb.com/interfaces
* Data extraction: http://imdbpy.sourceforge.net/
* Data storage: SQLite 3.8
* Data transformation: SQL
* Modelling framework: scikit-learn (Python 3.4)

## Algorithms

* Number of movies: 30349
* Minial votes: 1000
* Baseline (mean rating) MSE: 1.8115

### ElasticNet

Optimal L1-ratio was found to be equal to 1 so model turn out to be a pure Lasso.

I used 10-fold cross-validation on a training set (80% of input data). 20% of input dat formed test set for final model estimation.

* MSE on training set 1.5932
* MSE on testing set: 1.7052

### XGBoost

Optimal model had only 50 estimators.

I used 3-fold cross-validation on a training set (80% of input data). 20% of input dat formed test set for final model estimation.

* MSE on training set 1.2871
* MSE on testing set: 1.3541
