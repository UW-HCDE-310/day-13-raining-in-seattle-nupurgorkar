import urllib
#import json
from flask import Flask

app = Flask(__name__)






def is_it_raining_in_seattle():
    with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
        is_it_raining_in_seattle = response.read().decode()

    if is_it_raining_in_seattle == "true":
        return "Yes!"
    else:
        return "No!"

@app.route('/')
def hello():
    return is_it_raining_in_seattle()
