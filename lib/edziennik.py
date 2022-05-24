from pickle import PicklingError


class Edziennik:
    def __init__(self, credentials_dir, **kwargs):
        self.token = kwargs["vulcan_token"]
        self.symbol = kwargs["vulcan_symbol"]
        self.pin = kwargs["vulcan_pin"]
        self.credentials_dir = credentials_dir
