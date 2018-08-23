#!/usr/bin/python3
'''
    Handles cities
'''


from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models import BaseModel
from models.city import City


@app_views.route('/cities', methods=['GET'])
@app_views.route('/cities/<city_id>', methods=['GET'])
def cities_get(city_id=None):
    '''
        Returns a list of all cities, or specific city based on id
    '''
    list_of_dicts = []
    for k, v in storage.all('City').items():
        if city_id == BaseModel.to_dict(v)['id']:
            return jsonify(BaseModel.to_dict(v))
        list_of_dicts.append(BaseModel.to_dict(v))
    if city_id:
        abort(404)
    return jsonify(list_of_dicts)


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def cities_delete(city_id=None):
    '''
        Deletes a city object
        Not accounting for DELETE request with no city_id
    '''
    for k, v in storage.all('City').items():
        if city_id == BaseModel.to_dict(v)['id']:
            storage.delete(v)
            storage.save()
            return jsonify({}), 200
    abort(404)


@app_views.route('/cities', methods=['POST'])
def cities_post():
    '''
        Creates a city object
    '''
    data = request.get_json()
    if not data:
        return jsonify(error='Not a JSON'), 400
    if 'name' not in data:
        return jsonify(error='Missing name'), 400
    new_obj = City(**data)
    new_obj.save()
    return jsonify(new_obj.to_dict()), 201
