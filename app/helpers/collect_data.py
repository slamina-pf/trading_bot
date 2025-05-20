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

    def collect_data(self):

        data = BINANCE_NORMAL_CONNECTION.fetch_ohlcv(self.symbol, self.timeframe, limit=self.limit)
        df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        return df
    
    def run(self):
        df = self.collect_data()
        print("Data collected: ", df.describe())
        return df
