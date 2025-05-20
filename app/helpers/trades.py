from app.helpers.connections import BINANCE_NORMAL_CONNECTION

def get_balance(currency: str = "USDT"):
    balance = BINANCE_NORMAL_CONNECTION.fetch_balance()
    return balance['total'][currency]

def calculate_quantity(balance: float, percentage: float = 0.1):
    quantity = balance * percentage
    return quantity

def get_precision_and_minimus(symbol: str):
    market = BINANCE_NORMAL_CONNECTION.load_markets()[symbol]
    precision = market['precision']
    minimus = market['limits']['amount']['min']
    return precision, minimus

def create_market_order(symbol: str, side: str, quantity: float):
    order = BINANCE_NORMAL_CONNECTION.create_market_order(symbol, side, quantity)
    return order

