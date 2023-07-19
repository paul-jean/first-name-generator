from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import random
import json

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load transition matrix from JSON file
with open('transition_matrix.json', 'r') as f:
    transition_matrix = json.load(f)

@app.route('/generate_name', methods=['GET'])
def generate_name():
    length = int(request.args.get('length', 5))  # Default length is 5
    name = ''
    current_char = random.choice(list(transition_matrix.keys()))  # Start with a random character
    name += current_char

    for _ in range(length - 1):
        next_char = np.random.choice(
            list(transition_matrix[current_char].keys()),
            p=list(transition_matrix[current_char].values())
        )
        name += next_char
        current_char = next_char

    return jsonify({'name': name.capitalize()})


if __name__ == '__main__':
    app.run(debug=True)

