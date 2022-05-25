from pickle import PicklingError


from vulcan import Keystore
from vulcan import Account
from vulcan import Vulcan

class Edziennik:
    def __init__(self, credentials_dir,):
        self.credentials_dir = credentials_dir
