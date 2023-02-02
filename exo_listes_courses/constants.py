import os

CUR_DIR = os.path.dirname(os.path.abspath(__file__)) #os.path.abspath chemin absolu 
DATA_DIR = os.path.join(CUR_DIR, "data")
print(DATA_DIR) #afficher le chemin 