from sklearn.base import BaseEstimator, TransformerMixin


class GroupbyImputer(BaseEstimator, TransformerMixin):
    """Groupby Imputer
    
    """
    def __init__(self, by=None, column=None, strategy='mean'):
        self.by = by
        self.column = column
        self.strategy = strategy
        
        if self.strategy not in ['mean', 'median']:
            raise ValueError('')
    
    def fit(self, X, y=None):
        X = X.copy()
        
        return self
    
    def transform(self, X):
        X = X.copy()
        X.groupby(by=self.by)[column].agg(self.strategy)
        pass