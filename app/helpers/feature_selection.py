
##Im keeping this as a class, im thinking in the feature we can handle different types of feature selection based on the model.

class FeatureSelection:

    def select_features(self, df):
        features = ["sma_200", "rsi", "macd_histogram", "macd_signal"]
        selected_features = df[features]

        return selected_features
    

    def run(self, df):
        selected_features = self.select_features(df)

        return selected_features