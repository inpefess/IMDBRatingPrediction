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

### Mean rating for all (baseline)

* RMSE: 1.3447
* Mean absolute error: 1.0475
* Median absolute error: 0.8883

### ElasticNet

Optimal L1-ratio was found to be equal to 1 so model turn out to be a pure Lasso.

I used 10-fold cross-validation on a training set (80% of input data). 20% of input dat formed test set for final model estimation.

* RMSE: 1.3036
* Mean absolute error: 1.0259
* Median absolute error: 0.8547

### XGBoost

Optimal model had 800 estimators with maximal depth of intercation being equal to 10.

I used 3-fold cross-validation on a training set (60% of input data). 40% of input dat formed test set for final model estimation.

* RMSE: 0.7232
* Mean absolute error: 0.4695
* Median absolute error: 0.2818

### SVR

Optimal Support Vector Machine Regressor has a RBF kernel (linear kernel prooved extremely ineffective for this problem) and parameters C = 4, epsilon = 0.05
I used 3-fold cross-validation on a training set (60% of input data). 40% of input dat formed test set for final model estimation.

* RMSE: 1.3298
* Mean absolute error: 1.0313
* Median absolute error: 0.8036
