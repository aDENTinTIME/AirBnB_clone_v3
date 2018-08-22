#!/usr/bin/python3
'''
    index
'''

from api.v1.views import app_views
from flask import jsonify
import models
from models import storage


@app_views.route('/status')
def status():
    '''
        Returns status in json format
    '''
    return jsonify(status="OK")


@app_views.route('/stats')
def stats():
    '''
        Returns stats in json format
    '''
    dic = {'amenities': storage.count('Amenity'),
            'cities': storage.count('Citie'),
            'places': storage.count('Place'),
            'reviews': storage.count('Review'),
            'states': storage.count('State'),
            'users': storage.count('User')}
    return jsonify(dic)
