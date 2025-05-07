import redis
import ccxt
from helpers.constants import API_KEY, SECRET

BINANCE_NORMAL_CONNECTION = ccxt.binance()

EXCHANGE = ccxt.binance({
    'apiKey': API_KEY,
    'secret': SECRET,
    'enableRateLimit': True,
    'options': {'defaultType': 'spot'},
})

EXCHANGE.set_sandbox_mode(True)
EXCHANGE.enableRateLimit = True

redis_server = redis.Redis(host='redis', port=6379, db=0)