from flask import Flask, render_template, request, jsonify
from crew.main import create_project

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['POST', 'GET'])
def input():
    if request.method == 'POST':
        data = request.get_json()
        if 'idea' in data and 'type' in data:
            project_type = data['type']
            project_idea = data['idea']
            dev_result = create_project(project_type, project_idea)
            print(dev_result)
            return jsonify({'project_type': project_type, 'project_idea': project_idea, 'response': dev_result})
        else:
            return jsonify({'error': 'Invalid data'})
    else:
        return render_template('input.html')    

if __name__ == '__main__':
    app.run(debug=True)