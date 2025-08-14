from flask import Flask, render_template
import datetime
import math # Import math for floor function

app = Flask(__name__)

@app.route('/')
def home():
    # Set your specific launch date and time here
    launch_date_obj = datetime.datetime(2025, 8, 16, 9, 0, 0)
    
    # Calculate the time remaining (in seconds)
    now = datetime.datetime.now()
    distance_seconds = (launch_date_obj - now).total_seconds()

    # Ensure distance is not negative (if launch date has passed)
    if distance_seconds < 0:
        distance_seconds = 0

    # Calculate days, hours, minutes, and seconds from the total seconds
    days = math.floor(distance_seconds / (60 * 60 * 24))
    hours = math.floor((distance_seconds % (60 * 60 * 24)) / (60 * 60))
    minutes = math.floor((distance_seconds % (60 * 60)) / 60)
    seconds = math.floor(distance_seconds % 60)

    # Pass all calculated values to the HTML template
    return render_template('index.html', 
                           days=days, 
                           hours=hours, 
                           minutes=minutes, 
                           seconds=seconds,
                           # Also pass a flag to indicate if the launch date has passed
                           is_live=distance_seconds <= 0)

if __name__ == '__main__':
    # When running locally, Flask development server might not always detect 'templates'
    # It's better to run with gunicorn for consistency with Render:
    # gunicorn app:app -b 0.0.0.0:5000
    app.run(debug=True)