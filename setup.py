import pandas as pd
import numpy as np
from flask import Flask, render_template, request, url_for
import joblib
from scipy.io import arff

# Declare a Flask app
app = Flask(__name__, template_folder='flaskr/templates',
            static_folder='flaskr/static')

attribute_information = {
"a":"Area (A): The area of a bean zone and the number of pixels within its boundaries.",
"P":"Perimeter (P): Bean circumference is defined as the length of its border.",
"L":"Major axis length (L): The distance between the ends of the longest line that can be drawn from a bean.",
"l":"Minor axis length (l): The longest line that can be drawn from the bean while standing perpendicular to the main axis.",
"K":"Aspect ratio (K): Defines the relationship between L and l.",
"Ec":"Eccentricity (Ec): Eccentricity of the ellipse having the same moments as the region.",
"C":"Convex area (C): Number of pixels in the smallest convex polygon that can contain the area of a bean seed.",
"Ed":"Equivalent diameter (Ed): The diameter of a circle having the same area as a bean seed area.",
"Ex":"Extent (Ex): The ratio of the pixels in the bounding box to the bean area.",
"S":"Solidity (S): Also known as convexity. The ratio of the pixels in the convex shell to those found in beans.",
"R":"Roundness (R): Calculated with the following formula: (4piA)/(P^2)",
"CO":"Compactness (CO): Measures the roundness of an object: Ed/L",
"SF1":"ShapeFactor1 (SF1)",
"SF2":"ShapeFactor2 (SF2)",
"SF3":"ShapeFactor3 (SF3)",
"SF4":"ShapeFactor4 (SF4)",
"Class":"Class (Seker, Barbunya, Bombay, Cali, Dermosan, Horoz and Sira)",
}

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
        prediction = X.to_numpy()

    else:
        prediction = pd.DataFrame(np.zeros([1,17]))

    return render_template("input_data.html", output=prediction)

@app.route('/', methods=['GET', 'POST'])
@app.route('/dataset', methods=['GET', 'POST'])
def dataset():
    # converting csv to html
    dataset_path = 'flaskr/static/assets/datasets/Dry_Bean_Dataset.arff'
    dataset = arff.loadarff(dataset_path)
    df = pd.DataFrame(dataset[0])
    df = df.head(15).iloc[1:, 0:]
    df.columns = ["A","P","L","l","K","Ec","C","Ed","Ex","S","R","CO","SF1","SF2","SF3","SF4", "Class"]
    return render_template('dataset.html', tables=[df.to_html(notebook=True, table_id="dataset", classes="table", index=False)], columns_name=df.columns, attribute_names=attribute_information)
# ------------------


# Running the app
if __name__ == '__main__':
    app.run(debug=True)

# Class Seker, Barbunya, Bombay, Cali, Dermosan, Horoz and Sira
