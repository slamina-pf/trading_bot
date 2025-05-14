
##Im keeping this as a class, im thinking in the feature we can handle different types of feature selection based on the model.

class FeatureSelection:

    def select_features(self, df):
        features = ["sma_200", "rsi", "macd_histogram", "macd_signal"]
        X = df[features]
        Y = df["label"]

        return X, Y
    

    def run(self, df):
        X, Y = self.select_features(df)

        return X, Y