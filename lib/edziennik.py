from pickle import PicklingError


class Edziennik:
    def __init__(self, datadir, **kwargs):
        self.token = kwargs["vulcan_token"]
        self.symbol = kwargs["vulcan_symbol"]
        self.pin = kwargs["vulcan_pin"]
        self.datadir = datadir
