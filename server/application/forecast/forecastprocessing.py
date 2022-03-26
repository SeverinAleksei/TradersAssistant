from datetime import datetime

import numpy as np
import yfinance as yf
from flask import Blueprint
from flask import jsonify
from flask import request
from flask_jwt_extended import jwt_required
from statsmodels.tsa.stattools import adfuller

from application import jwt

# Blueprint Configuration

forecastprocessing_bp = Blueprint(
    'forecastprocessing_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@forecastprocessing_bp.route("/getforecastoptions", methods=["GET"])
@jwt_required()
def getforecastoptions():
    # We can now access our sqlalchemy User object via `current_user`.
    print("get options")
    options = {}
    options['product'] = [{'value': 'BTC-USD', 'label': 'BTC-USD'},
                          {'value': 'MSFT', 'label': 'MSFT'},
                          {'value': 'AAPL', 'label': 'AAPL'}]
    options['timeframe'] = [{'value': '1m', 'label': '1m'},
                            {'value': '5m', 'label': '5m'},
                            {'value': '1h', 'label': '1h'},
                            {'value': '1d', 'label': '1d'}]
    options['transformation'] = [{'value': 'first-difference',
                                  'label': 'first-difference'},
                                 {'value': 'Natural logarithm',
                                  'label': 'Natural logarithm'},
                                 {'value': 'No transformation',
                                  'label': 'No transformation'}]

    options['model'] = [{'value': 'ARIMA',
                         'label': 'ARIMA'},
                        {'value': 'SARIMA',
                         'label': 'SARIMA'}]
    return jsonify(options)


@forecastprocessing_bp.route("/getpricedata", methods=["POST"])
@jwt_required()
def getpricedata():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data.get('from'))
        data_down = yf.download(tickers=post_data.get('product'), start=str(post_data.get('from')[0:10]),
                                interval=post_data.get('timeframe'))
        # print(data_down)
        response_object['out'] = []
        print("Download of data is ended")
        print("---------------")
        for i in range(len(list(data_down["Open"].values))):
            response_object['out'].append([datetime.timestamp(data_down.index[i]) * 1000,
                                           data_down["Open"].values[i]])

    print("End of price data processing")
    return jsonify(response_object)


@forecastprocessing_bp.route("/gettransformation", methods=["POST"])
@jwt_required()
def gettransformation():
    response_object = {'status': 'success'}
    print("transformation")
    if request.method == 'POST':
        post_data = request.get_json()

        data_down = yf.download(tickers=post_data.get('product'), start=str(post_data.get('from')[0:10]),
                                interval=post_data.get('timeframe'))
        # print(data_down)
        response_object['out'] = []
        if post_data.get('transformation') == 'first-difference':
            for i in range(1, len(data_down["Open"].values)):
                response_object['out'].append([datetime.timestamp(data_down.index[i]) * 1000,
                                               data_down["Open"].values[i] - data_down["Open"].values[i - 1]])
        elif post_data.get('transformation') == 'Natural logarithm':
            data_down["log"] = 100 * np.log(data_down["Open"])
            for i in range(1, len(data_down["Open"].values)):
                response_object['out'].append([datetime.timestamp(data_down.index[i]) * 1000,
                                               data_down["log"].values[i] - data_down["log"].values[i - 1]])

        elif post_data.get('transformation') == 'No transformation':
            for i in range(1, len(data_down["Open"].values)):
                response_object['out'].append([datetime.timestamp(data_down.index[i]) * 1000,
                                               data_down["Open"].values[i]])

        fullerresult = adfuller([i[1] for i in response_object['out']])
        response_object['adfstat'] = fullerresult[0]
        response_object['pvalue'] = fullerresult[1]
    return jsonify(response_object)


@forecastprocessing_bp.route("/getmaxstep", methods=["POST"])
@jwt_required()
def getmaxstep():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    out = '0'

    if post_data['product'] != '' and post_data['timeframe'] != '' and post_data['from'] != '':
        if post_data['transformation'] != '':
            if post_data['model'] != '':
                if post_data['modelparameters'] != '':
                    out = '4'
                else:
                    out = '3'
            else:
                out = '2'
        else:
            out = '1'
    else:
        out = '0'

    return out

@forecastprocessing_bp.route("/getonlypricetransformation", methods=["POST"])
@jwt_required()
def getonlypricetransformation():
    response_object = {'status': 'success'}
    print("transformation")
    if request.method == 'POST':
        print("only price transformation")
        post_data = request.get_json()
        print("----------------------")
        data_down = yf.download(tickers=post_data.get('product'), start=str(post_data.get('from')[0:10]),
                                interval=post_data.get('timeframe'))
        # print(data_down)
        response_object['transformed'] = []
        transformed = []
        if post_data.get('transformation') == 'first-difference':
            for i in range(1, len(data_down["Open"].values)):
                transformed.append(data_down["Open"].values[i] - data_down["Open"].values[i - 1])

        elif post_data.get('transformation') == 'Natural logarithm':
            data_down["log"] = 100 * np.log(data_down["Open"])
            for i in range(1, len(data_down["Open"].values)):
                transformed.append(data_down["log"].values[i] - data_down["log"].values[i - 1])

        elif post_data.get('transformation') == 'No transformation':
            for i in range(1, len(data_down["Open"].values)):
                transformed.append(data_down["Open"].values[i])

        response_object['transformed'] = transformed
        response_object['train'] = transformed[0: round(len(transformed)*post_data.get('traintestsplit')/100)]
        response_object['test'] = transformed[round(len(transformed)*post_data.get('traintestsplit')/100):]

    return jsonify(response_object)
