import pickle

def save_embeddings(path,data):

    with open(path,"wb") as f:
        pickle.dump(data,f)

def load_embeddings(path):

    with open(path,"rb") as f:
        return pickle.load(f)