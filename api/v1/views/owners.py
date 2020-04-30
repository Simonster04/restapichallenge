#!/usr/bin/python3
""" Amenity """
from flask import Flask, jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.owner import Owner


@app_views.route('/owners', methods=["GET", "POST"],
                 strict_slashes=False)
def list_owners():
    """ Owners' list """
    if request.method == "GET":
        owners = storage.all("Owner")
        owners_dict = []
        for owner in owners.values():
            owners_dict.append(owner.to_dict())
        return jsonify(owners_dict)
    if request.method == "POST":
        data = request.get_json()
        if data is None:
            abort(400, "Not a JSON")
        if "first_name" not in data:
            abort(400, "Missing first_name")
        if "last_name" not in data:
            abort(400, "Missing last_name")
        new_owner = Owner(**data)
        new_owner.save()
        return jsonify(new_owner.to_dict()), 201


@app_views.route('/owners/<owner_id>', methods=["GET", "DELETE", "PUT"],
                 strict_slashes=False)
def owner(owner_id=None):
    """ Owner """
    owner = storage.get("Owner", owner_id)
    if owner is None:
        abort(404)
    if request.method == "GET":
        return jsonify(owner.to_dict())
    if request.method == "DELETE":
        owner.delete()
        storage.save()
        return jsonify({}), 200
    if request.method == "PUT":
        data = request.get_json()
        if data is None:
            abort(400, "Not a JSON")
        for key, value in data.items():
            if key != "id" and key != "created_at" and key != "updated_at"\
                    and key != "email" and hasattr(owner, key):
                setattr(owner, key, value)
        storage.save()
        return jsonify(owner.to_dict()), 200
