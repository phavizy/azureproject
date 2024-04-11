from flask import Flask, render_template
import requests
import random
import time

app = Flask(__name__)

# Azure Maps subscription key
subscription_key = 'VEC8jnHVVpp0189S0UhDXGia3hw1iVPGRNU-bVn0dTE'

# Points A, B, and C coordinates (latitude, longitude)
points = {
    'A': {'name': 'Seattle', 'coords': '47.6062,-122.3321'},  # Example coordinates for Seattle
    'B': {'name': 'San Francisco', 'coords': '37.7749,-122.4194'},  # Example coordinates for San Francisco
    'C': {'name': 'Los Angeles', 'coords': '34.0522,-118.2437'}   # Example coordinates for Los Angeles
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate')
def simulate():
    route = calculate_route()
    return route

def calculate_route():
    start_point, end_point = random.sample(points.keys(), 2)
    url = f'https://atlas.microsoft.com/route/directions/json?subscription-key={subscription_key}&api-version=1.0&query={points[start_point]["coords"]}:{points[end_point]["coords"]}&travelMode=car'
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(debug=True)
