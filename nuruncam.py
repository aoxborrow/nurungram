import os
from flask import Flask

# take a sip
app = Flask(__name__)

# default route
@app.route('/')
def index():
	return 'Hello Nurun!'