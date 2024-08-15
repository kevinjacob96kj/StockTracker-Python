class Strike:
    ticker : str = ''
    strikePrice: float = 0.00
    expDate: str = ''
    type: str = ''
    avgPrice: float = 0.00
    qty: int = 0
    currentPrice: float = 0.00
    iv: str = ''
    openInterest: int = 0
    bid: int = 0.00 
    ask: int = 0.00
    mid: int = 0.00
    intrinsicValue: int = 0.00
    extrinsicValue: int = 0.00
    profitLoss: float = 0.00
    priceToBook: float = 0.00
    targetLowPrice: float = 0.00
    targetMedianPrice: float = 0.00
    targetHighPrice: float = 0.00
    fiftyTwoWeekLow: float = 0.00
    fiftyTwoWeekHigh: float = 0.00

    def __init__(self, holding):
        self.ticker = holding[0].upper()
        self.strikePrice = float(holding[1])
        self.expDate = holding[2]
        self.type = holding[3].upper()
        self.avgPrice = float(holding[4])
        self.qty = int(holding[5])

    def setCurrentPrice(self, currentPrice):
        self.currentPrice = currentPrice

    def setOptionsData(self, data):
        self.iv = data['Implied Volatility']
        self.openInterest = data['Open Interest']
        self.bid = data['Bid']
        self.ask = data['Ask']
        self.mid = (self.ask + self.bid)/2

    def setStockData(self, info):
        self.priceToBook = info['priceToBook']
        self.targetLowPrice = info['targetLowPrice']
        self.targetMedianPrice = info['targetMedianPrice']
        self.targetHighPrice = info['targetHighPrice']
        self.fiftyTwoWeekLow = info['fiftyTwoWeekLow']
        self.fiftyTwoWeekHigh = info['fiftyTwoWeekHigh']

    def print(self):
        print(f'ticker: {self.ticker}')
        print(f'strikePrice: {self.strikePrice:.2f}')
        print(f'expDate: {self.expDate}')
        print(f'type: {self.type}')
        print(f'avgPrice: {self.avgPrice:.2f}')
        print(f'currentPrice: {self.currentPrice:.2f}')
        print(f'iv: {self.iv}')
        print(f'openInterest: {self.openInterest}')
        print(f'bid: {self.bid:.2f}')
        print(f'ask: {self.ask:.2f}')
        print(f'mid: {self.mid:.2f}')
        print(f'intrinsicValue: {self.intrinsicValue:.2f}')
        print(f'extrinsicValue: {self.extrinsicValue:.2f}')
        print(f'profit Loss per contract: {self.profitLoss:.2f}')
        print(f'total profit Loss: {self.qty * self.profitLoss:.2f}')
        print(f'priceToBook: {self.priceToBook:.2f}')
        print(f'targetLowPrice: {self.targetLowPrice:.2f}')
        print(f'targetMedianPrice: {self.targetMedianPrice:.2f}')
        print(f'targetHighPrice: {self.targetHighPrice:.2f}')
        print(f'fiftyTwoWeekLow: {self.fiftyTwoWeekLow:.2f}')
        print(f'fiftyTwoWeekHigh: {self.fiftyTwoWeekHigh:.2f}')

        print('=======================')
