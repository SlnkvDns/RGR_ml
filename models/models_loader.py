import pickle
from catboost import CatBoostClassifier 

class ModelsLoader:
    def load_dtc(self, path = r"DecisionTreeCl.pkl"):
        with open(path, "rb") as f:
            return pickle.load(f).best_estimator_
        
    
    def load_gbc(self, path = r"XGBoostClassifier.pkl"):
        with open(path, "rb") as f:
            return pickle.load(f).best_estimator_
        

    def load_cbc(self, path = r"CatBoostClassifier2"):
        from_file = CatBoostClassifier()
        from_file.load_model(path, format="cbm")
        return from_file
        

    def load_rfc(self, path = r"RandomForestClassifier.pkl"):
        with open(path, "rb") as f:
            return pickle.load(f).best_estimator_
        

    def load_stacking(self, path = r"StackingClassifier.pkl"):
        with open(path, "rb") as f:
            return pickle.load(f)
