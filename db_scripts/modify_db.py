class DBModifier:
    def __init__(self):
        self.actions = {
            'import_suggested_portfolio': self.import_suggested_portfolio,
            'show_current_portfolio': self.show_current_portfolio,
            'show_sell_buy': self.show_sell_buy,
            'show_suggested_portfolio': self.show_suggested_portfolio,
            'delete_recreate_db': self.delete_recreate_db,
            'import_current_portfolio': self.import_current_portfolio,
        }

    def import_suggested_portfolio(self):
        self._log_action("Import ERSTE market portfolio is running")

    def show_current_portfolio(self):
        self._log_action("Show current portfolio is running")

    def show_sell_buy(self):
        self._log_action("Show Sell & Buy is running")

    def show_suggested_portfolio(self):
        self._log_action("Suggested Portfolio is running")

    def delete_recreate_db(self):
        self._log_action("Delete and Recreate DB is running")

    def import_current_portfolio(self):
        self._log_action("Import Current Portfolio is running")

    def _log_action(self, message):
        print(message)
