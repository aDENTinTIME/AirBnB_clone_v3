#!/usr/bin/python3
'''
    app
'''


from flask import Flask
from api.v1.views import app_views
from os import getenv
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.teardown_appcontext
def teardown(self):
    '''
        Tears-down app
    '''
    storage.close()

if __name__ == "__main__":
    hosti = getenv("HBNB_API_HOST", default="0.0.0.0")
    porti = getenv("HBNB_API_PORT", default=5000)
    app.run(host=hosti, port=porti, threaded=True)
