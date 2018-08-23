#!/usr/bin/python3
'''
    views
'''

from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views.index import *  # noqa
from api.v1.views.states import *  # noqa
from api.v1.views.city import *  # noqa
from api.v1.views.amenity import *  # noqa
from api.v1.views.user import *  # noqa
from api.v1.views.place import *  # noqa
from api.v1.views.reviews import *  # noqa
