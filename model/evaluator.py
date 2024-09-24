from sklearn.metrics import accuracy_score
from model.model import Model

class Evaluator:

    def evaluate(model, X_test, Y_test):

        predicoes = Model.preditor(model, X_test)
        
        return accuracy_score(Y_test, predicoes)
                
