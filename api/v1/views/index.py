#!/usr/bin/python3


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
        Returns status in json format
    '''
    dic = {}
    for x in models.classes:
        dic[x.lower()+'s'] = storage.count(x)
    return jsonify(dic)
