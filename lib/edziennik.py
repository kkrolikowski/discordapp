from pickle import PicklingError


class Edziennik:
    def __init__(self, token, symbol, pin):
        self.token = token
        self.symbol = symbol
        self.pin = pin
