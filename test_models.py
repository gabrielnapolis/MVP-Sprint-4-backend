from model import *

# To run: pytest -v test_models.py

# Parameters    
url_data = "./MachineLearning/data/test_dataset_heart_disease.csv"
columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak' , 'slope', 'ca', 'thal', 'target']

# Data loader
dataset = Loader.loading_data(url_data, columns)
array = dataset.values
X = array[:,0:-1]
y = array[:,-1]
 
# Method for testing SVM model from corresponding file
def test_modelo_svm():
    # Importing SVM model
    svm_path = './MachineLearning/models/svm_heart_disease_classifier.pkl'
    model_svm = Model.loader_model(svm_path)

    # Capture SVM metrics
    accuracy_svm = Evaluator.evaluate(model_svm, X, y)
    
    # Testing SVM metrics
    assert accuracy_svm >= 0.80

