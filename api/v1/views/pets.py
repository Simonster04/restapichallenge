#!/usr/bin/python3
""" States """
from flask import Flask, jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.pets import Pets


@app_views.route('/pets', methods=["GET", "POST"], strict_slashes=False)
def list_pets():
    """list pets"""
    if request.method == "GET":
        pets = storage.all("Pets")
        pets_dict = []
        for pet in pets.values():
            pets_dict.append(pet.to_dict())
        return jsonify(pets_dict)
    if request.method == "POST":
        data = request.get_json()
        if data is None:
            abort(400, "Not a JSON")
        if "name" not in data:
            abort(400, "Missing name")
        new_pet = Pets(**data)
        new_pet.save()
        return jsonify(new_pet.to_dict()), 201


@app_views.route('/pets/<pets_id>', methods=["GET", "DELETE", "PUT"],
                 strict_slashes=False)
def pet(pets_id=None):
    """pet"""
    petlist = storage.get("Pets", pets_id)
    if petlist is None:
        abort(404)
    if request.method == "GET":
        return jsonify(petlist.to_dict())
    if request.method == "DELETE":
        petlist.delete()
        storage.save()
        return jsonify({}), 200
    if request.method == "PUT":
        data = request.get_json()
        if data is None:
            abort(400, "Not a JSON")
        for key, value in data.items():
            if key != "id" and key != "created_at" and key != "updated_at"\
             and hasattr(petlist, key):
                setattr(petlist, key, value)
        storage.save()
        return jsonify(petlist.to_dict()), 200
