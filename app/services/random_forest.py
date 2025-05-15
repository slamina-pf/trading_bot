
class RandomForest:

    def __init__(
        self,
        data_collector,
        data_cleaning,
        feature_engineering,
        feature_selection
    ):
        self.data_collector = data_collector
        self.data_cleaning = data_cleaning
        self.feature_engineering = feature_engineering
        self.feature_selection = feature_selection

    def run(self):
        df = self.data_collector.run()

        df = self.data_cleaning.run(df)

        df = self.feature_engineering.run(df)

        df = self.feature_selection.run(df)

        return df

