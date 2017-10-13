"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, request, render_template
import requests
import json
import os

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route('/')
def hello_world():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("index.html") # Render the template located in "templates/index.html"

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("aboutUs.html")

@app.route('/blog/8-experiments-in-motivation')
def motivation():
    return render_template("motivation.html")

@app.route('/blog/a-mindful-shift-of-focus')
def focus():
    return render_template("focus.html")

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def direction():
    return render_template("direction.html")

@app.route('/blog/training-to-be-a-good-writer')
def writer():
    return render_template("writer.html")


@app.route('/blog/what-productivity-systems-wont-solve')
def productivity():
    return render_template("productivity.html")

@app.route('/form', methods=['POST'])
def post_form():
    data = json.loads(request.data.decode('ascii'))
    r = requests.post(
    "https://api.mailgun.net/v3/"+os.environ["INFO253_MAILGUN_DOMAIN"]+"/messages",
    auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"]),
    data = {"from": data['name'] + " " + os.environ["INFO253_MAILGUN_FROM_EMAIL"],
    'to': os.environ["INFO253_MAILGUN_TO_EMAIL"],
    'subject': data['subject'],
    'text': data['msg']})
    return(' ',204)

@app.route('/contact')
def contact():
    return render_template("contactUs.html")
