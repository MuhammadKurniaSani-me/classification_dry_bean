import pandas as pd
import numpy as np
from flask import Flask, render_template, request, url_for
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import joblib
from scipy.io import arff

import flaskr.models.model as model_value

# Declare a Flask app
app = Flask(__name__, template_folder='flaskr/templates',
            static_folder='flaskr/static')

attribute_information  = {
"a":"Area Luas zona kacang dan jumlah piksel di dalam batasnya.",
"P":"Perimeter Lingkar kacang didefinisikan sebagai panjang batasnya.",
"L":"Panjang sumbu utama Jarak antara ujung garis terpanjang yang dapat ditarik dari kacang.",
"l":"Panjang sumbu minor Garis terpanjang yang dapat ditarik dari kacang sambil berdiri tegak lurus terhadap sumbu utama.",
"K":"Rasio aspek  Mendefinisikan hubungan antara L dan l.",
"Ec":"Eccentricity Eksentrisitas elips yang memiliki momen yang sama dengan daerah.",
"C":"Area cembung Jumlah piksel dalam poligon cembung terkecil yang dapat memuat luas biji kacang.",
"Ed":"Equivalent diameter Diameter lingkaran yang luasnya sama dengan luas biji kacang.",
"Ex":"Extent Rasio piksel dalam kotak pembatas ke area kacang.",
"S":"Soliditas Juga dikenal sebagai konveksitas. Rasio piksel dalam cangkang cembung dengan yang ditemukan dalam kacang.",
"R":"Kebulatan Dihitung dengan rumus berikut: (4piA)/(P^2)",
"CO":"Kekompakan Mengukur kebulatan objek: Ed/L",
"SF1":"Shape Factor1",
"SF2":"Shape Factor2",
"SF3":"Shape Factor3",
"SF4":"Shape Factor4",
"Kelas":"Kelas (0 : Seker, 1 : Barbunya, 2 : Bombay, 3 : Cali, 4 : Dermosan, 5 : Horoz, 6 : Sira)",
}

# Main function here


@app.route('/', methods=['GET', 'POST'])
@app.route('/input', methods=['GET', 'POST'])
def input():

    navbar_active = "classifier_navbar"
    class_value_list = ["Seker", "Barbunya", "Bombay", "Cali", "Dermosan", "Horoz", "Sira"]
    prediction_class = 0

    # If a form is submitted
    if request.method == "POST":

        # Unpickle classifier
        clf = joblib.load("./flaskr/static/trained_models/model_neigh.pkl")

        # Get values through input bars
        area = request.form.get("area")
        perimeter = request.form.get("perimeter")
        major_axis_length = request.form.get("major_axis_length")
        minor_axis_length = request.form.get("minor_axis_length")
        aspect_ratio = request.form.get("aspect_ratio")
        eccentricity = request.form.get("eccentricity")
        convex_area = request.form.get("convex_area")
        equivalent_diameter = request.form.get("equivalent_diameter")
        extent = request.form.get("extent")
        solidity = request.form.get("solidity")
        roundness = request.form.get("roundness")
        compactness = request.form.get("compactness")
        shape_factor1 = request.form.get("shape_factor1")
        shape_factor2 = request.form.get("shape_factor2")
        shape_factor3 = request.form.get("shape_factor3")
        shape_factor4 = request.form.get("shape_factor4")

        # Put inputs to dataframe
        X = pd.DataFrame([[area, perimeter, major_axis_length, minor_axis_length, aspect_ratio, eccentricity, convex_area, equivalent_diameter, extent, solidity, roundness, compactness, shape_factor1, shape_factor2, shape_factor3, shape_factor4]], columns=[
                         "area", "perimeter", "major_axis_length", "minor_axis_length", "aspect_ratio", "eccentricity", "convex_area", "equivalent_diameter", "extent", "solidity", "roundness", "compactness", "shape_factor1", "shape_factor2", "shape_factor3", "shape_factor4"])

        # Get prediction
        prediction_aray = X.to_numpy()

        # Scaller
        scaler = StandardScaler()
        scaler.fit(prediction_aray)
        data_nilai_transformed = scaler.transform(prediction_aray.reshape(1, -1))
        prediction_class = clf.predict(data_nilai_transformed)[0]


    else:
        prediction_class = None 


    return render_template("input_data.html", output=prediction_class, class_value_list=class_value_list, navbar_post=navbar_active)

@app.route('/dataset', methods=['GET', 'POST'])
def dataset():

    navbar_active = "dataset_navbar"

    # converting csv to html
    dataset_path = 'flaskr/static/assets/datasets/Dry_Bean_Dataset.arff'
    dataset = arff.loadarff(dataset_path)
    df = pd.DataFrame(dataset[0])
    df = df.head(15).iloc[1:, 0:]
    df.columns = ["A","P","L","l","K","Ec","C","Ed","Ex","S","R","CO","SF1","SF2","SF3","SF4", "Class"]
    return render_template('dataset.html', tables=[df.to_html(notebook=True, table_id="dataset", classes="table", index=False)], columns_name=df.columns, attribute_names=attribute_information, navbar_post=navbar_active)

@app.route('/preproccessing', methods=['GET', 'POST'])
def preproccessing():

    navbar_active = "preproccessing_navbar"

    ### CONSTANT
    FIRST_IDX = 0
    RAND_STATE = 123

    dataset_path = 'flaskr/static/assets/datasets/Dry_Bean_Dataset.arff'
    dataset = arff.loadarff(dataset_path)
    df = pd.DataFrame(dataset[0])
    X = df.drop(columns=["Class"])
    y = df['Class'].values
    le = LabelEncoder()
    le.fit(y)
    y = le.transform(y)
    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)

    # converting csv to html
    df = pd.DataFrame(X)
    df = df.head(15).iloc[1:, 0:]
    df.columns = ["A","P","L","l","K","Ec","C","Ed","Ex","S","R","CO","SF1","SF2","SF3","SF4"]
    return render_template('preproccessing.html', tables=[df.to_html(notebook=True, table_id="dataset", classes="table", index=False)], columns_name=df.columns, attribute_names=attribute_information, navbar_post=navbar_active)

@app.route('/modelling', methods=['GET', 'POST'])
def modelling():

    navbar_active = "modelling_navbar"
    accuracy_values = model_value.accuracy_values

    return render_template('modelling.html', navbar_post=navbar_active, acc_values=accuracy_values)
# ------------------


# Running the app
if __name__ == '__main__':
    app.run(debug=True)

# Class Seker, Barbunya, Bombay, Cali, Dermosan, Horoz and Sira
