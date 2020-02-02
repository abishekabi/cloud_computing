from flask import Flask
from flask import jsonify

app = Flask(__name__)

APP_VERSION = 2.0

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/<value>')
def api(value):
    return jsonify({"api_param": value})

@app.route('/api/version')
def api_version():
    return 'Api version: %s' %(str(APP_VERSION))

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
