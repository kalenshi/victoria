import os
from victoria import creat_app

DEBUG = os.environ.get("FLASK_DEBUG", True)
PORT = os.environ.get("PORT", 5000)

app = creat_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
