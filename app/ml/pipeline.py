from sklearn.model_selection import train_test_split
from app.ml.preprocessor import Preprocessor
from app.ml.feature_selector import FeatureSelector
from app.ml.evaluator import Evaluator
from app.ml.models import LogisticModel, RandomForestModel, BaggingClassifier, SVC, GaussianNB, KNeighborsClassifier

class ChurnPipeline:

    def __init__(self, algorithm: str):
        self.model = self._select_model(algorithm)
        self.preprocessor = Preprocessor()
        self.selector = FeatureSelector()
        self.evaluator = Evaluator()

    def _select_model(self, algo):
        if algo == "logistic":
            return LogisticModel()
        elif algo == "random_forest":
            return RandomForestModel()
        elif algo == "bagging":
            return BaggingClassifier()
        elif algo == "svc":
            return SVC()
        elif algo == "gaussian_nb":
            return GaussianNB()
        elif algo == "knn":
            return KNeighborsClassifier()
        else:
            raise ValueError("Unsupported algorithm")

    def execute(self, df, target):
        X = df.drop(columns=[target])
        y = df[target]

        X = self.preprocessor.fit_transform(X)
        X = self.selector.select(X, y)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        self.model.train(X_train, y_train)
        preds = self.model.predict(X_test)

        return self.evaluator.evaluate(y_test, preds)
