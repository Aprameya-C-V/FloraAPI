from flask import Flask, jsonify, request

app = Flask(__name__)

plants_data = {
    "rose": {
        "watering_schedule": "Every 7 days",
        "care_tips": "Place in a sunny spot",
        "troubleshooting": "Yellowing leaves may indicate overwatering."
    },
    "snake_plant": {
        "watering_schedule": "Every 14 days",
        "care_tips": "Thrives in low light conditions",
        "troubleshooting": "Browning tips could be due to overwatering."
    },
    # Add more plant entries here
}

users = {
    "user123": {
        "password": "password",
        "plants": ["rose", "snake_plant"]
    }
}

@app.route('/plants/<string:plant_name>', methods=['GET'])
def get_plant_info(plant_name):
    if plant_name in plants_data:
        return jsonify(plants_data[plant_name])
    else:
        return jsonify({"error": "Plant not found"}), 404

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username]['password'] == password:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/user/plants', methods=['GET'])
def get_user_plants():
    username = request.headers.get('username')
    if username in users:
        return jsonify({"plants": users[username]['plants']})
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/user/plants/<string:plant_name>', methods=['POST'])
def add_user_plant(plant_name):
    username = request.headers.get('username')
    if username in users and plant_name in plants_data:
        users[username]['plants'].append(plant_name)
        return jsonify({"message": f"{plant_name} added to your plants"})
    else:
        return jsonify({"error": "User or plant not found"}), 404

@app.route('/user/plants/<string:plant_name>', methods=['DELETE'])
def remove_user_plant(plant_name):
    username = request.headers.get('username')
    if username in users and plant_name in users[username]['plants']:
        users[username]['plants'].remove(plant_name)
        return jsonify({"message": f"{plant_name} removed from your plants"})
    else:
        return jsonify({"error": "User or plant not found"}), 404

# Additional features

@app.route('/user/plants/<string:plant_name>/reminders', methods=['POST'])
def set_plant_reminder(plant_name):
    # Implement setting reminders for plant care tasks
    # Return a success message
    pass

@app.route('/user/plants/<string:plant_name>/care-history', methods=['GET'])
def get_plant_care_history(plant_name):
    # Implement retrieving care history for a plant
    # Return a list of care activities
    pass

@app.route('/user/plants/<string:plant_name>/share-tips', methods=['POST'])
def share_plant_care_tip(plant_name):
    # Implement sharing care tips about a plant
    # Return a success message
    pass

@app.route('/user/plants/<string:plant_name>/care-plan', methods=['POST'])
def set_custom_care_plan(plant_name):
    # Implement setting a custom care plan for a plant
    # Return a success message
    pass

@app.route('/user/plants/<string:plant_name>/image-upload', methods=['POST'])
def upload_plant_image(plant_name):
    # Implement image upload for plant recognition
    # Return recognition results or confirmation
    pass

# Implement other additional features similarly

if __name__ == '__main__':
    app.run(debug=True)
