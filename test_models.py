from model import *

# To run: pytest -v test_models.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "./MachineLearning/data/test_dataset_heart_disease.csv"
colunas = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak' , 'slope', 'ca', 'thal', 'target']

# Carga dos dados
dataset = Carregador.carregar_dados(url_dados, colunas)
array = dataset.values
X = array[:,0:-1]
y = array[:,-1]
 
# Método para testar modelo SVM a partir do arquivo correspondente
def test_modelo_svm():
    # Importando modelo de SVM
    svm_path = './MachineLearning/models/svm_heart_disease_classifier.pkl'
    modelo_svm = Model.carrega_modelo(svm_path)

    # Obtendo as métricas do KNN
    acuracia_svm = Avaliador.avaliar(modelo_svm, X, y)
    
    # Testando as métricas do SVM
    assert acuracia_svm >= 0.80

