#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
#日本語文字化け対応
app.config['JSON_AS_ASCII'] = False

# root
@app.route('/', methods=['GET'])
def index():
    return 'Hello World'

# GET Request
@app.route('/api/<key>', methods=['GET'])
def get(key):
    return jsonify({'items': key})

# Get book data
@app.route('/books/api', methods=['GET'])
def get_books():
    model = read_book_model()
    if model is None:
        return "NOT FOUND"
    else:
        return jsonify(model)

# Model Layer
# Get books model from json file
def read_book_model():
    try:
        with open('books.json', 'r') as f:
            return json.load(f)
    except IOError as e:
        print(e)
        return None

# Main
if __name__ == '__main__':
    app.run(debug=True)
