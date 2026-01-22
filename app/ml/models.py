from sklearn.linear_model import LogisticRegression as LR
from sklearn.ensemble import RandomForestClassifier as RFC
from app.ml.base import BaseModel 
from sklearn.ensemble import BaggingClassifier as BC
from sklearn.svm import SVC as svc_model
from sklearn.naive_bayes import GaussianNB as GNB
from sklearn.neighbors import KNeighborsClassifier as KNN

class LogisticModel(BaseModel):

    def __init__(self):
        self.model = LR(max_iter=1000)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)


class RandomForestModel(BaseModel):

    def __init__(self):
        self.model = RFC()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
    

class BaggingClassifier(BaseModel):

    def __init__(self):
        self.model = BC()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)


class SVC(BaseModel):

    def __init__(self):
        self.model = svc_model()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
    
class GaussianNB(BaseModel):

    def __init__(self):
        self.model = GNB()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
    

class KNeighborsClassifier(BaseModel):

    def __init__(self):
        self.model = KNN()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)