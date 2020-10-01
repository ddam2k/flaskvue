from flask import Flask, request, jsonify
from flask_cors import CORS
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')
data = {
    "fields": ['host', 'cpu', 'mem', 'hdd'],
    "data": [
        {'host':'wgkim', 'cpu':'30', 'mem':'1800', 'hdd':'20'},
        {'host':'bwlee', 'cpu':'40', 'mem':'1500', 'hdd':'30'},
        {'host':'mgkim', 'cpu':'50', 'mem':'2000', 'hdd':'40'},
    ]
}

# CORS(app)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/rest/get')
def rest_get():
    return jsonify(data)

@app.route('/rest/set', methods = ['POST'])
def rest_set():
    req = request.get_json()
    print(req)
    for idx in range(len(data["data"])):
        if(data["data"][idx]['host'] == req["key"]):
            data["data"][idx] = req["row"]
            break
    return jsonify(req)

if __name__ == "__main__":
    app.run()