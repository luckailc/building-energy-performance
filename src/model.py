from model_factory import ModelFactory
from sklearn.tree import DecisionTreeClassifier


@ModelFactory.register_model("logistic_regression")
class DecisionTreeModel:

    def __init__(self, cfg):

        self.model = DecisionTreeModel()

    def fit(self, x_train, y_train):

        self.model.fit(x_train, y_train)

    def predict(self, x_test):

        return self.model.predict(x_test)

    def score(self, x_test, y_test):

        return self.model.score(x_test, y_test)
