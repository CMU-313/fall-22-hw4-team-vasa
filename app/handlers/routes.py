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

    @app.route('/predict')
    def predict():
        #use entries from the query string here but could also use json
        G1 = request.args.get('G1')
        G2 = request.args.get('G2')
        absences = request.args.get('absences')
        studytime = request.args.get('studytime')

        if not str.isdigit(G1):
            return jsonify({}), 400

        if not str.isdigit(absences):
            return jsonify({}), 400

        if not str.isdigit(studytime):
            return jsonify({}), 400

        data = [[G1], [G2], [absences], [studytime]]
        query_df = pd.DataFrame({
            'G1': pd.Series(G1),
            'G2': pd.Series(G2),
            'absences': pd.Series(absences),
            'studytime': pd.Series(studytime)
        })
        
        prediction = clf.predict(query_df)
        return jsonify(np.ndarray.item(prediction))

