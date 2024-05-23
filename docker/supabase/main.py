import os
from flask import Flask, jsonify, request
from supabase import create_client, Client

url: str = os.getenv('SUPABASE_URL')
key: str = os.getenv('SUPABASE_KEY')

supabase: Client = create_client(url, key)

app = Flask(__name__)
@app.route('/items', methods=['GET'])
def index():
    response = supabase.table('users').select('*').execute()
    print(response)
    return jsonify(response.data)