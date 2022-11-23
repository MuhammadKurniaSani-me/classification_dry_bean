import pandas as pd
import numpy as np
from flask import Flask, render_template, request, url_for
import joblib
from scipy.io import arff

# Declare a Flask app
app = Flask(__name__, template_folder='flaskr/templates',
            static_folder='flaskr/static')

# Main function here


@app.route('/', methods=['GET', 'POST'])
@app.route('/input', methods=['GET', 'POST'])
def input():

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
        prediction = X

    else:
        prediction = pd.DataFrame(np.zeros([1,17]))

    # return render_template("input_data.html", output=prediction)
    return render_template('input_data.html', tables=[prediction.to_html()], titles=['sdsd'])

@app.route('/', methods=['GET', 'POST'])
@app.route('/dataset', methods=['GET', 'POST'])
def dataset():
    # converting csv to html
    dataset_path = 'flaskr/static/assets/datasets/Dry_Bean_Dataset.arff'
    dataset = arff.loadarff(dataset_path)
    df = pd.DataFrame(dataset[0])
    df = df.head(10)
    return render_template('dataset.html', tables=[df.to_html()], titles=[''])
# ------------------


# Running the app
if __name__ == '__main__':
    app.run(debug=True)
