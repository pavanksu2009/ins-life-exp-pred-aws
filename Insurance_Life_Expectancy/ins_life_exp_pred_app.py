
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, json, jsonify

filename = "models/challa_linear_reg.sav"
load_model = joblib.load(filename)

def predict_single(data, model):
    X = pd.DataFrame([data])
    y_pred = model.predict(X)
    return y_pred[0]

app = Flask(__name__)

@app.route('/predict', methods= ['POST'])
def predict():
    data = request.get_json()
    prediction = predict_single(data, load_model)
    
    result = {
        'Predicted_Value' : prediction
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port= 3333)
        

    
    

