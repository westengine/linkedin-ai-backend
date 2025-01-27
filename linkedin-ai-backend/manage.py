# manage.py


import os
from flask.cli import FlaskGroup
from project.server import create_app

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

app = create_app(os.getenv("FLASK_CONFIG") or "default")
# cli = FlaskGroup(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

print(app.url_map)