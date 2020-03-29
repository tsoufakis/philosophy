#! /usr/bin/python

import json
from philosophy import find_philosophy
from flask import Flask
app = Flask(__name__)

@app.route('/')
def say_hi():
    return 'Hello There!\n'

@app.route('/phil/<path:wiki_url>')
def phil(wiki_url):
    result = find_philosophy(wiki_url)
    return json.dumps(result) + '\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
