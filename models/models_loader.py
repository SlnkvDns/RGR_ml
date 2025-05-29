import pickle
from catboost import CatBoostClassifier 

class ModelsLoader:
    def load_dtc(self, path = r"models/DecisionTreeCl.pkl"):
        with open(path, "rb") as f:
            return pickle.load(f).best_estimator_
        
    
    def load_gbc(self, path = r"models/XGBoostClassifier.pkl"):
        with open(path, "rb") as f:
            return pickle.load(f).best_estimator_
        

    def load_cbc(self, path = r"models/CatBoostClassifier2"):
        from_file = CatBoostClassifier()
        from_file.load_model(path, format="cbm")
        return from_file
        

    def load_rfc(self, path = r"models/RandomForestClassifier.pkl"):
        with open(path, "rb") as f:
            return pickle.load(f).best_estimator_
        

    def load_stacking(self, path = r"models/StackingClassifier.pkl"):
        with open(path, "rb") as f:
            return pickle.load(f)

    def load_fcnn(self, path = r"models/FCNN.pkl"):
        with open(path, "rb") as f:
            return pickle.load(f)