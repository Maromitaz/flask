from flask import Flask
from routes import Routes 

app = Flask(__name__)

@app.route("/")
def index():
    return Routes.index_route()

if __name__ == "__main__":
    app.run()
