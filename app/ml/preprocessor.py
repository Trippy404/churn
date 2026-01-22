import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

class Preprocessor:

    def __init__(self):
        self.scaler = StandardScaler()
        self.encoders = {}

    def fit_transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()

        for col in X.select_dtypes(include="object"):
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col])
            self.encoders[col] = le

        X[X.columns] = self.scaler.fit_transform(X)
        return X
