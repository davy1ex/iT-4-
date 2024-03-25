from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    data = request.get_json()
    print(json.dumps(data, indent=4))  # Pretty print the received JSON data
    return jsonify({"message": "Data received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)
