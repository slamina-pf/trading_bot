from celery import shared_task
from app.helpers.connections import redis_server
from app.services.random_forest import RandomForest
from app.helpers.collect_data import DataCollector
from app.helpers.clean_data import DataCleaning
from app.helpers.feature_engineering import FeatureEngineering
from app.helpers.feature_selection import FeatureSelection

@shared_task(name="app.tasks.trading.random_forest_5m_task")
def random_forest_5m_task():
    bot_active = redis_server.get('random_forest_5m')

    data_collector = DataCollector(
        symbol="BTC/USDT",
        timeframe="5m",
        limit=200
    )

    data_cleaning = DataCleaning()

    feature_engineering = FeatureEngineering()

    feature_selection = FeatureSelection()
    print("bot_active: ", bot_active)
    if bot_active:
        random_forest = RandomForest(
            data_collector=data_collector,
            data_cleaning=data_cleaning,
            feature_engineering=feature_engineering,
            feature_selection=feature_selection
        )
        random_forest_result=random_forest.run()
        print("random_forest_result: ", random_forest_result)
        return random_forest_result

