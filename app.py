from flask import Flask

# Create the Flask application
app = Flask(__name__)

# Home endpoint
@app.route("/")
def home():
    return "Hello from Python Flask CI/CD Project!"

# Health endpoint
@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "python-flask-app"
    }

# Start the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)