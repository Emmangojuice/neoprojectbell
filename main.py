from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.exceptions import HTTPException
import os 
from your_tracking_module import track_delivery # # Assume a module to handle delivery tracking

# App factory
def create_app():
    app = Flask(__name__)
    
    # Configuration (Optional: Load from environment or config file)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key')
    
    # Define application routes

    # Home route: Displays the main landing page
    @app.route('/')
    def home():
        return render_template('index.html')

    # Track route: Handles GET and POST requests for tracking deliveries
    @app.route('/track', methods=['GET', 'POST'])
    def track():
        if request.method == 'POST':
            # Retrieve the tracking number from the form input
            tracking_number = request.form.get('tracking_number')
            if not tracking_number:
                # Return an error message if no tracking number is provided
                return render_template('track.html', error="Please provide a tracking number.")

            try:
                status = track_delivery(tracking_number)
                if "error" in status:
                    # Return an error message if tracking fails or no status is available
                    return render_template(track.html, error=status["error"])

                # Render the results page with the delivery status 
                return render_template("result.html", status=status)
            except Exception as e: 
                # Handle any exceptions and display a friendly error message
                return render_template("track.html", error=f"Error tracking delivery: {str(e)}")

        # Render the tracking page for GET requests
        return render_template('track.html')

    # Error handler: Handles HTTP exceptions and displays an error page
    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        return render_template('error.html', code=e.code, description=e.description), e.code

    return app

# Create the app instance
app = create_app()

if __name__ == "__main__":
    # Run the application in debug mode for development
    app.run(debug=True)
