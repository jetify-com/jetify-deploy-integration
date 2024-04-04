import os
import redis
from flask import Flask, jsonify, request


redis_cache = redis.StrictRedis(
    host=os.getenv('REDIS_HOST'),
    password=os.getenv('REDIS_PASSWORD'),
    port=os.getenv('REDIS_PORT'),
    ssl=True
)

app = Flask(__name__)

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    redis_cache.set(item['name'], item['value'])
    return jsonify({'message': 'Item added successfully'})

@app.route('/<string:item>')
def index(item):
    if redis_cache.exists(item):
        return jsonify({'response': redis_cache.get(item).decode('utf-8')})
    else:
        return jsonify({'message': f"{item} not found"})