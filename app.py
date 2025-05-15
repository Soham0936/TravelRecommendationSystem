from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load datasets
tourism_data = pd.read_csv('data/tourism_with_id.csv')
tourism_rating = pd.read_csv('data/tourism_rating.csv')
user_data = pd.read_csv('data/user.csv')

# Define a recommendation function
def recommend_places(user_id):
    # Basic collaborative filtering logic for demonstration
    user_ratings = tourism_rating[tourism_rating['user_id'] == user_id]
    if user_ratings.empty:
        return []

    recommended = tourism_data[~tourism_data['place_id'].isin(user_ratings['place_id'])]
    return recommended.head(5).to_dict(orient='records')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = int(request.form['user_id'])
    recommendations = recommend_places(user_id)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
