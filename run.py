import os
from victoria import app

DEBUG = os.environ.get("FLASK_DEBUG", True)
PORT = os.environ.get("PORT", 5000)

if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)