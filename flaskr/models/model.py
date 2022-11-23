# Data PATH
import sys

# Data Wrangling
import pandas as pd
import numpy as np
from scipy.io import arff


# Modelling
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Remove unnecessary warnings
import warnings
warnings.filterwarnings('ignore')


# Add project file PATH
project_home = 'home/mxsani/Documents/progamming/python/Environment/classification/'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Load Data
dataset_url = "flaskr/static/assets/datasets/Dry_Bean_Dataset.arff"
data = arff.loadarff(dataset_url)
df = pd.DataFrame(data[0])

# CONSTANT
FIRST_IDX = 0
RAND_STATE = 123

# Spilt Data
X = df.drop(columns=["Class"])
y = df['Class'].values

le = LabelEncoder()
le.fit(y)
y = le.transform(y)

scaler = StandardScaler().fit(X)
X = scaler.transform(X)


def run_experiment(model, X_train_param, y_train_param):
    """
        get every metric score from a model
    """
    model.fit(X_train_param, y_train_param)

    y_pred = model.predict(X_test)
    accuracy_score_result = accuracy_score(y_test, y_pred)
    print('Accuracy: %.3f' % accuracy_score_result)
    return accuracy_score


percent_amount_of_test_data = 0.3
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=percent_amount_of_test_data, random_state=0)

model_dtc = DecisionTreeClassifier()
run_experiment(model_dtc, X_train, y_train)


model_gnb = GaussianNB()
run_experiment(model_gnb, X_train, y_train)

n_neighbors = 5
model_neigh = KNeighborsClassifier(n_neighbors=n_neighbors)
run_experiment(model_neigh, X_train, y_train)


model_lr = LogisticRegression(random_state=RAND_STATE).fit(X, y)
run_experiment(model_lr, X_train, y_train)


joblib.dump(model_dtc, "flaskr/static/trained_models/model_dtc.pkl")
joblib.dump(model_gnb, "flaskr/static/trained_models/model_gnb.pkl")
joblib.dump(model_neigh, "flaskr/static/trained_models/model_neigh.pkl")
joblib.dump(model_lr, "flaskr/static/trained_models/model_lr.pkl")
