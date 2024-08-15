import warnings
from csvReader import *
from engine import * 
from object import Strike 
import yfinance as yf

warnings.simplefilter(action='ignore', category=FutureWarning)

def main():
  holdings = readFromCSV()
  optionChain = []

  for holding in holdings:
    strike = Strike(holding)
    setStockPrice(strike)
    setOptionsData(strike)
    setIntrinsicExtrensicValue(strike)
    setProfitLoss(strike)

  strike.print()

main()