
from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(quotes, self).__init__(action)

    def index(self):
        return self.load_view('index.html')
