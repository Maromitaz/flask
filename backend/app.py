from utils import sanitize_str

from flask import Flask
import sqlite3, traceback, sys

app = Flask(__name__)

@app.route("/api/")
def api_index():
    return "<h1>API</h1>"

@app.route("/api/create", methods=["POST"])
def api_create():
    con = sqlite3.connect("./CRUD.db")
    cur = con.cursor()
    try:
        cur.execute(sanitize_str(""))
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    con.close()
    return ""