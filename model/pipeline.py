import numpy as np
import pickle

class Pipeline:
    
    def loading_pipeline(path):
        """Loading pipeline build on training phase
        """
        
        with open(path, 'rb') as file:
             pipeline = pickle.load(file)
        return pipeline