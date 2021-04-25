"""
Ethan Pressley's Flask API.
"""

from flask import Flask, abort, render_template, send_from_directory
import os

app = Flask(__name__)

# default webpage
@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

# request handler if a path is given
@app.route("/<path:directory>")
def handleRequest(directory):
    # if there is a forbidden character, abort to 403 error
    if "~" in directory or ".." in directory or "//" in directory:
        abort(403)

    # otherwise check if pages/<directory> is a file
    elif os.path.isfile(os.path.join("pages", directory)): 
        return send_from_directory("pages", directory), 200
    
    # if it is not it does not exist, abort to 404 error
    else:
        abort(404)

# simple error handler for 403
@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403

# simple error handler for 404
@app.errorhandler(404)
def notFound(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
