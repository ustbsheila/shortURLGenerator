import os
from app import create_app

# Get the Flask app instance using the application factory pattern
app = create_app()

if __name__ == "__main__":
    # Run the app on the development server
    app.run(host="0.0.0.0", port=os.getenv('PORT', 8080), debug=True)