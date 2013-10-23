import os
from flask import Flask, render_template
from instagram import client

# take a sip
app = Flask(__name__)
app.config['DEBUG'] = True

# instagram client
INSTAGRAM_CLIENT_ID = '3bf6b1d83a6a428a85c72ca3e1be8143'
INSTAGRAM_CLIENT_SECRET = 'ed7d7293228241f089992803adcb4d4a'

# location id for "Nurun"
INSTAGRAM_LOCATION_ID = '854982'

# location id for "Tenderloin National Forest"
# INSTAGRAM_LOCATION_ID = '4365396'

# unauthenticated Instagram API
api = client.InstagramAPI(
	client_id = INSTAGRAM_CLIENT_ID, 
	client_secret = INSTAGRAM_CLIENT_SECRET
)

# default route, when no location defined, use Nurun
@app.route('/', defaults={'location_id': INSTAGRAM_LOCATION_ID})
@app.route('/<int:location_id>')
def index(location_id):

	# get location info
	location = api.location(location_id)

    # setup view fields
	view = {}
	view['title'] = location.name
	view['lat'] = str(location.point.latitude)[:-3] # i hate accuracy
	view['lon'] = str(location.point.longitude)[:-2]
	view['media'], next = api.location_recent_media(count = 30, location_id = location_id)
	
	# render view
	return render_template('index.j2', **view)

# for running from CLI
if __name__ == '__main__':
    app.run()