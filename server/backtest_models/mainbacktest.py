from simplemodels import simple_forecast_grid_search
from etsmodels import ets_forecast_grid_search
from mlpmodel import mlp_forecast_grid_search
from sarimamodels import sarima_forecast_grid_search
from pandas import read_csv
import yfinance as yf

#series = read_csv('monthly-mean-temp.csv', header=0, index_col=0)
#data = series.values
#data = data[-(5*12):]
#simple = simple_forecast_grid_search(20, range(1,13),data,12)
#ets = ets_forecast_grid_search([0,6,12], data[:,0],12)
#data = data[-(5*12):]

#sarima = sarima_forecast_grid_search([0,12], data, 12)
#for i in sarima:
#    print (i[0], i[1])



data_down = yf.download(tickers="BTC-USD", start="2019-09-01",
                                interval="1d")

data = data_down["Close"].values

simple = simple_forecast_grid_search(2, range(1,3),data,80)
#ets = ets_forecast_grid_search([0,6,7,30], data,80)
mlp = mlp_forecast_grid_search(data,80)

for i in simple:
    print (i[0], i[1])

#for i in ets:
#    print (i[0], i[1])

for i in mlp:
    print (i[0], i[1])