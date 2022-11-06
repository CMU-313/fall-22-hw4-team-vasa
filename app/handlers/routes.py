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
        absences = request.args.get('absences')
        studytime = request.args.get('studytime')

        if not str.isdigit(age):
            return jsonify({}), 400

        if not str.isdigit(absences):
            return jsonify({}), 400

        if not str.isdigit(studytime):
            return jsonify({}), 400

        if int(age) >= 18:
            data = [[age], [absences], [studytime]]
            query_df = pd.DataFrame({
                'age': pd.Series(age),
                'absences': pd.Series(absences),
                'studytime': pd.Series(studytime)
            })
            # query = pd.get_dummies()
            prediction = clf.predict(query_df)
            print(jsonify(np.ndarray.item(prediction)))
            print(int(age)>18)
            return jsonify(np.ndarray.item(prediction))
        else:
            # data = [[age], [absences], [studytime]]
            # query_df = pd.DataFrame({
            #     'age': pd.Series(age),
            #     'absences': pd.Series(absences),
            #     'studytime': pd.Series(studytime)
            # })
            # # query = pd.get_dummies()
            # prediction = clf.predict(query_df)
            # print(jsonify(np.ndarray.item(prediction)))
            # print(int(age)>18)
            # # return jsonify(np.ndarray.item(prediction))
            return "Welcome user, you have been rejected because you are too young!"


        # else:
        #     return 
    
    # @app.route('/train')
    # def train():

    # @app.route('/wipe', methods=['GET'])
    # def wipe():

