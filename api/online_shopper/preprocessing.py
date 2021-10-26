import pickle

from sklearn.preprocessing import LabelEncoder


def encoder_object(lst):
    le = LabelEncoder()
    le.fit(lst)

    return le


def save_object(object, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(object, file)


def load_object(file_path):
    with open(file_path, "rb") as file:
        return pickle.load(file)
