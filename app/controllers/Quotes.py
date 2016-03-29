
from system.core.controller import *

class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)
        self.load_model('Quote')

    def index(self):
        return self.load_view('index.html')

    def index_json(self):
        quotes = self.models['Quote'].all()
        return jsonify(quotes=quotes)

    def index_html(self):
        quotes = self.models['Quote'].all()
        return self.load_view('partials/quotes.html', quotes=quotes)
