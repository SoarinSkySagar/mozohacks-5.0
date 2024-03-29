from typing import List
from flask import Flask, render_template, request, jsonify
from crew.main import create_project
from flask_cors import CORS
from uuid import uuid4
from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv
from dataclasses import dataclass
from datetime import datetime

load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))
db = client.get_database("project_history")
collection = db["history"]

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@dataclass
class Event:
    timestamp: datetime
    data: str


@dataclass
class Job:
    project_type: str
    project_idea: str
    status: str
    events: List[Event]
    result: str


jobs = {}  # Dictionary to store Job objects (improved data structure)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/input', methods=['POST', 'GET'])
def input_data():
    if request.method == 'POST':
        data = request.get_json()
        if 'productIdea' in data and 'momma' in data:
            project_type = data['productIdea']
            project_idea = data['momma']
            req_id = str(uuid4())
            dev_result = create_project(project_type, project_idea)

            new_job = Job(
                project_type=project_type,
                project_idea=project_idea,
                status='COMPLETE',
                events=[],
                result=dev_result
            )
            jobs[req_id] = new_job  # Store Job object with complete status

            # Persist job data to MongoDB
            collection.insert_one(new_job.__dict__)  # Convert Job to dict for storage

            return jsonify({'req_id': req_id})
        else:
            return jsonify({'error': 'Invalid data'})
    else:
        return render_template('input.html')


@app.route('/api/crew/<req_id>', methods=['GET'])
def get_job_status(req_id):
    if req_id in jobs:
        job_data = jobs[req_id]
        return jsonify({
            'status': job_data.status,
            'events': [event.__dict__ for event in job_data.events],  # Convert events to dicts
            'result': job_data.result
        })
    else:
        return jsonify({'error': 'Invalid request ID'}), 404


if __name__ == '__main__':
    app.run(debug=True)
