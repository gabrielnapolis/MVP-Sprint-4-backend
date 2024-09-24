import pickle
from model.preprocessor import PreProcessor
class Model:
    
    def loader_model(path):
        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                model = pickle.load(file)
        else:
            raise Exception('Unsupported file format')
        return model
    
    def preditor(model, X_input):
        diagnosis = model.predict(X_input)
        return diagnosis