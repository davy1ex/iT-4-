from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    # Parse JSON data from request
    data = request.get_json()
    
    if data is None:
        return jsonify({"error": "No JSON received"}), 400
    
    # Extract userId from data
    user_id = data.get("userId")
    if not user_id:
        return jsonify({"error": "userId not provided"}), 400
    
    # File path based on userId
    file_path = f"{user_id}.json"
    
    # Write (or overwrite) the JSON data to the file
    with open(file_path, 'w') as file:
        # Pretty-print JSON data to file for readability
        json.dump(data, file, indent=4)
    
    return jsonify({"message": "Data received and saved"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)
