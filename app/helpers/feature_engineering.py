import ta

##Im keeping this as a class, im thinking in the feature we can handle different types of feature engineering based on the model.

class FeatureEngineering:

    def date_time_features(self, df):
        
        df['year'] = df['timestamp'].dt.year
        df['month'] = df['timestamp'].dt.month
        df['day'] = df['timestamp'].dt.day
        df['dayofweek'] = df['timestamp'].dt.dayofweek
        df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)

        return df
    
    def technical_indicators(self, df):

        df["sma_50"] = ta.trend.sma_indicator(df["close"], window=50)
        df["sma_200"] = ta.trend.sma_indicator(df["close"], window=200)
        df["ema_10"] = ta.trend.ema_indicator(df["close"], window=10)
        df["rsi"] = ta.momentum.RSIIndicator(df["close"], window=14).rsi()
        df["macd"] = ta.trend.macd(df["close"])
        df["macd_signal"] = ta.trend.macd_signal(df["close"])
        df["macd_histogram"] = ta.trend.macd_diff(df["close"])

        return df
    
    def drop_na(self, df):
        # Drop rows with NaN values
        df.dropna(inplace=True)
        return df
    
    def run(self, df):

        df = self.date_time_features(df)
        df = self.technical_indicators(df)
        df = self.drop_na(df)

        return df