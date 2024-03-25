from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    data = request.get_json()
    
    if data is None:
        print("No JSON received")
        return jsonify({"error": "No JSON received"}), 400
    print(json.dumps(data, indent=4))  # Pretty print the received JSON data
    return jsonify({"message": "Data received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)
