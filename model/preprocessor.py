from sklearn.model_selection import train_test_split
import pickle
import numpy as np

class PreProcessor:

    def separa_teste_treino(self, dataset, percentual_teste, seed=7):
        
        # division on training  and test
        X_train, X_test, Y_train, Y_test = self.__prepare_holdout(dataset,
                                                                  percentual_teste,
                                                                  seed)
        # normalization/standardization
        return (X_train, X_test, Y_train, Y_test)
    
    def __prepare_holdout(self, dataset, percentual_teste, seed):

        dados = dataset.values
        X = dados[:, 0:-1]
        Y = dados[:, -1]
        return train_test_split(X, Y, test_size=percentual_teste, random_state=seed)
    
    def prepare_form(form):
        X_input = np.array([
                            form['age'], 
                            form['sex'], 
                            form['cp'], 
                            form['trestbps'], 
                            form['chol'],
                            form['fbs'], 
                            form['restecg'], 
                            form['thalach'], 
                            form['exang'], 
                            form['oldpeak'], 
                            form['slope'], 
                            form['ca'], 
                            form['thal']
                        ])
        X_input = X_input.reshape(1, -1)
        return X_input
    
    def scaler(X_train):
        
        # normalization/standardization
        scaler = pickle.load(open('./MachineLearning/scalers/minmax_scaler_heart_disease.pkl', 'rb'))
        reescaled_X_train = scaler.transform(X_train)
        return reescaled_X_train
