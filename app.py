from flask import Flask
from config import configRoutes

app = Flask(__name__)

configRoutes(app)

if __name__ == "__main__":
    app.run()
