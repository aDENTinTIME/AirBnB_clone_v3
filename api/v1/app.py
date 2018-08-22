#!/usr/bin/python3
'''
    app
'''


from flask import Flask
from api.v1.views import app_views
from os import getenv
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    '''
        Tears-down app
    '''
    storage.close()

if __name__ == "__main__":
    hosti = getenv("HBNB_API_HOST", "0.0.0.0")
    porti = getenv("HBNB_API_PORT", 5000)
    app.run(host=hosti, port=porti, threaded=True)
