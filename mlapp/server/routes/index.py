from server import app
from flask import render_template, Flask, jsonify, request
import numpy as np
import pickle
import json
with open ('model.pkl', 'rb') as file:
    model = pickle.load(file)
@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return app.send_static_file('404.html')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
    return app.send_static_file('500.html')

@app.route("/classify", methods = ['GET'])
def classify():
    temperature = request.args.get('temperature', type=float)
    wind_speed = request.args.get('wind_speed', type=float)
    humidity = request.args.get('humidity', type=float)
    result = model.predict(np.array([[temperature, wind_speed, humidity]]).tolist()).tolist()
    #result = model.predict([[60., 3.54699666, 62.],[64., 3.72321496, 55.]])
    return jsonify({'risk': result}), 201