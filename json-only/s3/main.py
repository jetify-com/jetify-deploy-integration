import os
from flask import Flask, jsonify, request
import boto3

s3 = boto3.client('s3')

app = Flask(__name__)
@app.route('/items', methods=['GET'])
def index():
    response = s3.list_buckets()
    return jsonify(response)
