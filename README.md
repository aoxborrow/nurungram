##FLASK & HEROKU##
##Building NurunCam in only 243 easy steps!##

###Flask:###
	- a Python micro-framework for lightweight web apps
	- simple to start -- write your whole app in a single file
	- well suited for RESTful patterns
	- the right amount of features without bloat (BYODB)
	- Python <3

###Heroku:###
	- very clever cloud hosting for apps
	- free for small instances, easy to scale on demand
	- built around Git -- "git push" to deploy
	- CLI "toolbelt" and extensive API


### Python virtualenv & Hello World ###

1. Install Python. Oh, you're on a Mac? done.
	
7. Make your project folder and minimally a templates and static assets folder:
```
$ mkdir ~/www/nuruncam
$ mkdir ~/www/nuruncam/static
$ mkdir ~/www/nuruncam/templates
$ cd ~/www/nuruncam
```

2. Install pip (python package manager):
```
$ sudo easy_install pip
```

8. Install 'virtualenv' and create your app's Python virtual environment. This allows you to have an isolated environment with its own dependencies and helps make your app portable.
```
$ sudo pip install virtualenv
$ virtualenv venv --distribute
$ source venv/bin/activate   <--- activate your virtualenv
```
	
9. Install the Python packages we're going to use. We're gonna need Flask (the framework), Gunicorn (the web server), and the Python Instagram client. PIP will automatically install any other dependencies. Note -- these will only be installed in your lil' virtual environment.
```
(venv)$ pip install Flask gunicorn python-instagram
```

10. Finally some coding. Let's say hello.

**nuruncam.py**
```python
import os
from flask import Flask

# take a sip
app = Flask(__name__)

# default route
@app.route('/')
def index():
	return 'Hello Nurun!'
```

### Heroku, Git & Deployment ###


4. Create a free account at Heroku.com. Install the Heroku toolbelt

**https://toolbelt.heroku.com/**

11. Create a "Procfile" to tell Heroku how to run our web app:

**`Procfile`**
```
web: gunicorn nuruncam:app
```
		
12. Record the Python package requirements for Heroku:
```
(venv)$ pip freeze > requirements.txt
```

12. Use the Heroku tool "foreman" to start your app and test it in the browser.
```
(venv)$ foreman start 
(venv)$ open http://0.0.0.0:5000/
```
	
13. Let's start building our Git repo. Starting with a .gitignore file:
**`.gitignore`**
```
.DS_Store
venv
*.pyc
```
		
14. Init our Git Repo
```
(venv)$ git init
(venv)$ git add .
(venv)$ git commit -m "f1rst post"
```
	
15. Authenticate with Heroku via CLI and add your public key:
```
(venv)$ heroku login
(venv)$ heroku keys:add
```		

16. Create our Heroku app, supplying a unique name. Deploy!
```
(venv)$ heroku apps:create nuruncam
(venv)$ git push heroku master

-----> Compiled slug size: 28.7MB
-----> Launching... done, v3
       http://nuruncam.herokuapp.com deployed to Heroku
```

17. From the web dashboard you can monitor and scale your app resources, enable add-ons like MongoDB, New Relic, etc.
**https://addons.heroku.com/**

