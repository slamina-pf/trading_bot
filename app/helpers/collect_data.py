import pandas as pd
import time
from datetime import datetime, timedelta, timezone
from app.helpers.connections import BINANCE_NORMAL_CONNECTION
import pandas as pd

class DataCollector:
    def __init__(
            self, 
            symbol: str = "BTC/USDT", 
            timeframe: str = "5m",
            limit: int = 1000
        ):
        self.symbol = symbol
        self.timeframe = timeframe
        self.limit = limit
        self.end_date = datetime.now(timezone.utc)
        self.start_date = datetime.now(timezone.utc) - timedelta(days=365)

    def to_milliseconds(self, dt):
        return int(dt.timestamp() * 1000)

    def collect_data(self):

        since = self.to_milliseconds(self.start_date)
        end_timestamp = self.to_milliseconds(self.end_date)

        all_candles = []

        while since < end_timestamp:
            
            candles = BINANCE_NORMAL_CONNECTION.fetch_ohlcv(self.symbol, self.timeframe, since, self.limit)

            if not candles:
                break

            all_candles.extend(candles)

            since = candles[-1][0] + 1

            time.sleep(BINANCE_NORMAL_CONNECTION.rateLimit / 1000)
        
        return all_candles
    
    def run(self):
        data = self.collect_data()
        df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])

        return df
