import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model.pkl")
    clf = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "Welcome user!"
        #do we need to add status stuff here??


    @app.route('/predict')
    def predict():
        #use entries from the query string here but could also use json
        age = request.args.get('age')
        studytime = request.args.get('studytime')
        absences = request.args.get('absences')
        studytime = request.args.get('studytime')
        data = [[age], [studytime], [absences]]
        query_df = pd.DataFrame({
            'studytime': pd.Series(studytime),
            'absences': pd.Series(absences),
            'age': pd.Series(age)
        })
        # query = pd.get_dummies()
        prediction = clf.predict(query_df)
        return jsonify(np.ndarray.item(prediction))
    
    # @app.route('/train')
    # def train():

    # @app.route('/wipe', methods=['GET'])
    # def wipe():

