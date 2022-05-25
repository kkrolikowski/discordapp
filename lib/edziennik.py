from pickle import PicklingError


from vulcan import Keystore
from vulcan import Account
from vulcan import Vulcan

class Edziennik:
    def __init__(self, *args, **kwargs):
        self.token = kwargs["vulcan_token"]
        self.symbol = kwargs["vulcan_symbol"]
        self.pin = kwargs["vulcan_pin"]
        self.credentials_dir = args[0]
