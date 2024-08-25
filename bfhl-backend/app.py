from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# GET Method - Returns operation_code
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

# POST Method - Process input JSON and return response
@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        # Ensure the data is a list
        data = request.json.get('data', [])
        if not isinstance(data, list):
            return jsonify({"is_success": False, "error": "Data must be a list"}), 400
        
        # Separate numbers and alphabets
        numbers = [item for item in data if isinstance(item, str) and item.isdigit()]
        alphabets = [item for item in data if isinstance(item, str) and item.isalpha()]
        
        # Identify lowercase alphabets and find the highest one
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None
        
        # Construct response
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with actual user_id format
            "email": "prateekchoudhary1108@gmail.com",  # Replace with actual email
            "roll_number": "21BRS1450",  # Replace with actual roll number
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
