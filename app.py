from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for bus routes (you can replace this with a database)
bus_routes = {
    '101': 'Route 101 - Downtown to Airport',
    '202': 'Route 202 - Shopping Mall to Business District',
    '303': 'Route 303 - Residential Area to University',
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    route = request.form.get('route')
    passenger_name = request.form.get('name')
    
    if route and passenger_name:
        return f'Ticket booked for {passenger_name} on {bus_routes.get(route, "Unknown Route")}'
    else:
        return 'Invalid data. Please try again.'

if __name__ == '__main__':
    app.run(debug=True)
