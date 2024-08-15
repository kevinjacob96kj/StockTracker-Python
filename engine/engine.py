from yahoo_fin import options
import yfinance as yf
from object import Strike 

def setOptionsData(strike: Strike):
    if(strike.type == 'CALL'):
        allStrikes = options.get_calls(strike.ticker, strike.expDate).to_dict('split')
    strikeIndex = allStrikes['columns'].index('Strike')
    for data in allStrikes['data']:
        if(data[strikeIndex] == strike.strikePrice):
            strike.setOptionsData(convertStrikeToDict(data, allStrikes['columns'])) 
    
def convertStrikeToDict(values, columns):
    strike_dict = {}
    for key in columns:
        for value in values:
            strike_dict[key] = value
            values.remove(value)
            break
    return strike_dict

def setStockPrice(strike: Strike):
    info = yf.Ticker(strike.ticker).info
    strike.setCurrentPrice(info['currentPrice'])
    strike.setStockData(info)

def setIntrinsicExtrensicValue(strike: Strike):
    strike.intrinsicValue = strike.currentPrice - strike.strikePrice
    strike.extrinsicValue = strike.avgPrice - strike.intrinsicValue

def setProfitLoss(strike: Strike):
    strike.profitLoss = strike.mid - strike.avgPrice