from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')


def home():
    # Set your specific launch date and time here
    launch_date = datetime.datetime(2025, 8, 16, 9, 0, 0)
    
    # Pass the launch date to the HTML template
    return render_template('index.html', launch_date=launch_date.isoformat())

if __name__ == '__main__':
    app.run(debug=True)