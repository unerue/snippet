from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder


class CategoricalEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, one_hot=False):
        pass

    def fit(self, X, y=None):
        X = X.select_dtypes(include='category').copy()
        n_samples, n_features = X.shape
        
        if X.isnull().values.any():
            raise ValueError('dataframe has the missing values.')
        
        self._label_encoders = [LabelEncoder() for _ in range(n_features)]
        
        for i in range(n_features):
            le = self._label_encoders[i]
            le.fit(X.iloc[:, i])
            
        self._categories = [le.classes_ for le in self._label_encoders]
        
        return self
    
    def transform(self, X):
        X = X.select_dtypes(include='category').copy()
        n_samples, n_features = X.shape
        
        X_mask = np.ones_like(X, dtype=np.bool)

        for i in range(n_features):
            valid_mask = np.in1d(X.iloc[:, i], self._categories[i])
            
            if not np.all(valid_mask):
                raise ValueError('')
            else:
                X_mask[:, i] = valid_mask
                X.iloc[:, i][~valid_mask] = self._categories[i][0]
                X.iloc[:, i] = self._label_encoders[i].transform(X.iloc[:, i])

        return X