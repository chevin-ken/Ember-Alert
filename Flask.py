from flask import Flask, jsonify, request
import pickle
with open ('model', 'rb') as f:
    model = pickle.load(f)
app = Flask("__name__")
@app.route("/", methods = ['GET'])
def classify():
    temperature = request.args.temperature
    wind_speed = request.data.windSpeed
    humidity = request.data.humidity
    result = model.predict([temperature, windSpeed, humidity])
    return jsonify({'risk': result}), 201
if __name__ == '__main__':
    app.run(debug = True)