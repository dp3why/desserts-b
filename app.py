from app import app
import os

if __name__ == '__main__':
    # Get the TCP port on which the Flask app is running
    port = int(os.environ.get("PORT", 5000))
    print("Running on port:", port)

    # Start the Flask app
    app.run(host='0.0.0.0', port=port, debug=True)