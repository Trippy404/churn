from sklearn.feature_selection import SelectKBest, f_classif

class FeatureSelector:

    def select(self, X, y, k=10):
        selector = SelectKBest(score_func=f_classif, k=min(k, X.shape[1]))
        return selector.fit_transform(X, y)
