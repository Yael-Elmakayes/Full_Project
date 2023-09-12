from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Client']
users_collection = db['users']

@app.route('/add-user', methods=['POST'])
def add_user():
    # Get data from request
    data = request.json
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    phone = data['phone']
    password = data['pass']

    # Create user document
    user_doc = {
        'firstName': first_name,
        'lastName': last_name,
        'email': email,
        'phone': phone,
        'password': password
    }

    # Insert user document into MongoDB
    result = users_collection.insert_one(user_doc)

    # Return success message
    return {'message': 'User added successfully'}

if __name__ == '__main__':
    app.run(debug=True)