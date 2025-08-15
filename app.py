from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def countdown():
    # Set your launch date
    launch_date_obj = datetime.datetime(2025, 8, 15, 11, 10, 0)
    # Pass timestamp in milliseconds for JavaScript
    launch_timestamp = int(launch_date_obj.timestamp() * 1000)
    return render_template('index.html', launch_timestamp=launch_timestamp)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return "<h1>About Us</h1><p>We are awesome.</p>"

@app.route('/contact')
def contact():
    return "<h1>Contact Us</h1><p>Email: contact@example.com</p>"

if __name__ == '__main__':
    app.run(debug=True)
