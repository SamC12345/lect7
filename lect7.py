import flask
import os
import random

app = flask.Flask(__name__)
artists=[("Halsey","halsey.jpg"),("J Cole","jcole.jpg"),("TheFatRat","fatrat.jpg")]
@app.route('/')
def index():
    print("in indexsdf")
    return flask.render_template("index.html", len=len(artists), artists=artists, randomNum=random.randint(1,10))
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)