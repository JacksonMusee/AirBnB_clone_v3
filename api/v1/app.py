#!/usr/bin/python3
"""
Flask apllication return  status: OK
"""

import os
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Close the storage when app tear down/closes
    """
    storage.close()i


if __name__ == "__main__":
    """
    Start app
    """
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
