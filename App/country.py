from flask import Flask, request, jsonify
import services


def getAllCountries():
    results = services.getAllCountries()
    return jsonify(results)


