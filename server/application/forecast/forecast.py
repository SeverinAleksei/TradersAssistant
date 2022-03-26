import json

import pandas as pd
import requests
from flask import Blueprint
from flask import jsonify
from flask import request
from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm
from statsmodels.tsa.stattools import acf, pacf
import numpy as np
from application import jwt

# Blueprint Configuration

forecast_bp = Blueprint(
    'forecast_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@forecast_bp.route("/getACFPACF", methods=["POST"])
def forecast():
    # We can now access our sqlalchemy User object via `current_user`.
    response_object = {'status': 'success'}
    print("get acf pacf")
    if request.method == 'POST':
        post_data = request.get_json()
        print("get acf pacf post to forecastprocessing")
        url = 'http://192.168.1.69:5000/getonlypricetransformation'
        headers = {
            'Content-Type': "application/json",
            'Authorization': str("Bearer " + post_data.get('token'))
        }
        response = requests.request("POST", url, data=json.dumps(post_data.get('form')), headers=headers)
        transformed = response.json()['train']
        print("----")
        ticker_data_acf_1 = acf(transformed)[0:32]
        ticker_data_pacf_1 = pacf(transformed)[0:32]
        response_object['acf'] = list(ticker_data_acf_1)
        response_object['pacf'] = list(ticker_data_pacf_1)
    return jsonify(response_object)


@forecast_bp.route("/getarimaforecast", methods=["POST"])
def forecastarima():
    # We can now access our sqlalchemy User object via `current_user`.
    response_object = {'status': 'success'}
    print("ARIMA")
    if request.method == 'POST':
        post_data = request.get_json()
        url = 'http://192.168.1.69:5000/gettransformation'
        headers = {
            'Content-Type': "application/json",
            'Authorization': str("Bearer " + post_data.get('token'))
        }
        print('sending post request for transformed data (ARIMA)')
        response = requests.request("POST", url, data=json.dumps(post_data.get('form')), headers=headers)

        print(response.json())
        transformed = response.json()['out']
        data = pd.DataFrame(transformed, columns=['date','diff'])
        print(data)
        #train = response.json()['train']
        #test = response.json()['test']
        #print(train)
        #print(test)
        print("ARIMA further")
        print(post_data.get('form'))
        modelparameters = post_data.get('form')['modelparameters']
        X = data['diff'].values
        train = X[0:round(len(X) * post_data.get('form')['traintestsplit']/100)]
        test = X[round(len(X) * post_data.get('form')['traintestsplit']/100):]

        print('model parameters ARIMA ', modelparameters['ar'], modelparameters['i'], modelparameters['ma'])
        model = ARIMA(train,
                      order=(int(modelparameters['ar']), int(modelparameters['i']), int(modelparameters['ma'])))
        model_fit = model.fit()
        residuals = list(model_fit.resid)
        print(model_fit.summary())

        ar = int(modelparameters['ar'])
        ma = int(modelparameters['ma'])
        constant_param = model_fit.params[0]
        ar_params = model_fit.params[1:ar+1]
        ma_params = model_fit.params[ar+1:ar+1+ma]
        print(constant_param )
        print(ar_params)
        print(ma_params)
        test_forecast = []
        for i in range(len(train), len(X)):
            yhat = 0
            yhat = yhat + constant_param
            for j in range(1, ar + 1):
                yhat = yhat + ar_params[j-1]*X[i-j]

            for j in range(1, ma + 1):
                yhat = yhat + ma_params[j-1]* residuals[i-j]

            test_forecast.append(yhat)
            residuals.append(X[i] - yhat)


        #print(model_fit.predict())

        # print(residuals)
        response_object['train_residuals'] = list(model_fit.resid)
        response_object['train_predictions'] = list(model_fit.predict())
        response_object['train_actual'] = list(train)
        response_object['test_actual'] = list(test)
        response_object['test_predictions'] = test_forecast

        #response_object['summary'] = model_fit.summary()
        print("Accuracy ", np.sum(np.sign(response_object['test_predictions']) == np.sign(response_object['test_actual']))/ len(response_object['test_predictions']))
        #print(test)
        #fc,se,conf = model_fit.forecast(15, alpha = 0.05)
        #print(fc)
        print("----------------------------------")
        #print(response_object)
    return jsonify(response_object)
