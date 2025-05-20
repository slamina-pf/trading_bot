from app.helpers.trades import get_balance, calculate_quantity, get_precision_and_minimus
class ExecuteTrading:
    def __init__(
            self, 
            percentage: float = 0.01,
        ):
        self.percentage = percentage

    def execute(self):
        # Implement the logic to execute the trading strategy
        pass