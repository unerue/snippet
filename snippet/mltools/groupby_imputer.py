from sklearn.base import BaseEstimator, TransformerMixin


class GroupbyImputer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        pass