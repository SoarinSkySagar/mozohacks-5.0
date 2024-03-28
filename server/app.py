from flask import Flask, render_template, request, jsonify
from crew.main import create_project
from flask_cors import CORS
from uuid import uuid4
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))
db = client.get_database("project_history")
collection = db["history"]


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
jobs = {}  # Dictionary to store job data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['POST', 'GET'])
def input_data():
    if request.method == 'POST':
        data = request.get_json()
        if 'productIdea' in data and 'momma' in data:
            project_idea = data['productIdea']
            project_type = data['momma']
            req_id = str(uuid4())
            dev_result = create_project(project_type, project_idea)
            jobs[req_id] = {
                'project_type': project_type,
                'project_idea': project_idea,
                'status': 'COMPLETE',
                'events': [],
                'result': dev_result
            }
            collection.insert_one({
                'req_id': req_id,
                'project_type': project_type,
                'project_idea': project_idea,
                'result': dev_result
            })
            return jsonify({'req_id': req_id})
        else:
            return jsonify({'error': 'Invalid data'})
    else:
        return render_template('input.html')
    
@app.route('/api/crew/<req_id>')
def get_job_status(req_id):
    if req_id in jobs:
        job_data = jobs[req_id]
        return jsonify({
            'status': job_data['status'],
            'events': job_data['events'],
            'result': job_data['result']
        })
    else:
        return jsonify({'error': 'Invalid request ID'}), 404
    

if __name__ == '__main__':
    app.run(debug=True)