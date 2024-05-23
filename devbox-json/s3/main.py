import os
from flask import Flask, jsonify, request
import boto3

bucket: str = os.getenv("AWS_BUCKET_NAME")

s3 = boto3.client('s3')

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    response = s3.list_objects(Bucket=bucket)
    return jsonify(response)
