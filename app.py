from flask import Flask, jsonify

app = Flask(__name__)

# Placeholder data for plant care information
plants_data = {
    "rose": {
        "watering_schedule": "Every 7 days",
        "care_tips": "Place in a sunny spot",
        "troubleshooting": "Yellowing leaves may indicate overwatering."
    },
    # Add more plant entries here
}

@app.route('/plants/<string:plant_name>', methods=['GET'])
def get_plant_info(plant_name):
    if plant_name in plants_data:
        return jsonify(plants_data[plant_name])
    else:
        return jsonify({"error": "Plant not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
