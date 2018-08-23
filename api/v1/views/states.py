#!/usr/bin/python3
'''
    Handles states
'''


from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models import BaseModel
from models.state import State


@app_views.route('/states', methods=['GET'])
@app_views.route('/states/<state_id>', methods=['GET'])
def states_get(state_id=None):
    '''
        Returns a list of all states, or specific state based on id
    '''
    list_of_dicts = []
    for k, v in storage.all('State').items():
        if state_id == BaseModel.to_dict(v)['id']:
            return jsonify(BaseModel.to_dict(v))
        list_of_dicts.append(BaseModel.to_dict(v))
    if state_id:
        abort(404)
    return jsonify(list_of_dicts)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def states_delete(state_id=None):
    '''
        Deletes a state object
        Not accounting for DELETE request with no state_id
    '''
    for k, v in storage.all('State').items():
        if state_id == BaseModel.to_dict(v)['id']:
            storage.delete(v)
            storage.save()
            return jsonify({}), 200
    abort(404)


@app_views.route('/states', methods=['POST'])
def states_post():
    '''
        Creates a state object
    '''
    data = request.get_json()
    if not data:
        return jsonify(error='Not a JSON'), 400
    if 'name' not in data:
        return jsonify(error='Missing name'), 400
    new_obj = State(**data)
    new_obj.save()
    return jsonify(new_obj.to_dict()), 201
