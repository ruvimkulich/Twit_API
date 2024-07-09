from flask import Flask, json, jsonify, request

from model.twit import Twit

twits = []

app = Flask(__name__)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Twit):
            return {'body': obj.body, 'author': obj.author}
        else:
            return super().default(obj)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})


@app.route('/twit', methods=['POST'])
def creat_twit():
    '''{"body": "Hello World", "author": "@aqaguy"}
    '''
    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['author'])
    twits.append(twit)
    return jsonify({'status': 'success'})


@app.route('/twit', methods=['GET'])
def read_twits():
    return jsonify({'twits': twits})


if __name__ == '__main__':
    app.run(debug=True)