#Official Nurungram®#
###Learning Flask & Heroku in only 37 easy steps!###

###Flask:###
- a Python micro-framework for lightweight web apps, well suited for RESTful patterns
- simple to start -- write your whole app in a single file
- the right amount of features without bloat (BYODB, etc.)
- Python <3

###Heroku:###
- very clever cloud hosting for apps
- free for small instances, easy to scale on demand
- built around Git -- "git push" to deploy
- CLI "toolbelt" and extensive API


### 1. Python, virtualenv & Hello World ###

1. Install Python. Oh, you're on a Mac? done.
	
2. Make your project folder and minimally a static assets and templates folder:
```
$ mkdir ~/www/nurungram
$ mkdir ~/www/nurungram/static
$ mkdir ~/www/nurungram/templates
$ cd ~/www/nurungram
```

3. Install pip (python package manager):
```
$ sudo easy_install pip
```

4. Install `virtualenv` and create your app's Python virtual environment. This allows you to have an isolated environment with its own dependencies and helps make your app portable.
```
$ sudo pip install virtualenv
$ virtualenv venv --distribute
$ source venv/bin/activate   <--- activate your virtualenv
```
	
5. Install the Python packages you'll need. We're gonna want Flask (the framework), Gunicorn (the web server), and the Python Instagram client. PIP will automatically install any other dependencies. Note -- these will only be installed in your lil' virtual environment.
```
(venv)$ pip install Flask gunicorn python-instagram
```

6. Finally a little coding. Let's say hello in `nurungram.py`:

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

### 2. Heroku, Git & Initial Deployment ###


1. Create a free account at Heroku.com. Install the Heroku toolbelt:

	**https://toolbelt.heroku.com/**

2. Create a `Procfile` to tell Heroku how to run our web app:
```
web: gunicorn nurungram:app
```
		
3. Record the Python package requirements into `requirements.txt` for Heroku:
```
(venv)$ pip freeze > requirements.txt
```

4. Use the Heroku tool `foreman` to start your app and test it in the browser.
```
(venv)$ foreman start 
(venv)$ open http://0.0.0.0:5000/
```
	
5. Create your Git repo, starting with a `.gitignore` file:
```
.DS_Store
venv
*.pyc
```
		
6. Init your Git repo and make your first commit:
```
(venv)$ git init
(venv)$ git add .
(venv)$ git commit -m "f1rst p0st"
```
	
7. Authenticate with Heroku via CLI and add your public key:
```
(venv)$ heroku login
(venv)$ heroku keys:add
```		

8. Create our Heroku app, supplying a unique name. Deploy via Git(!), then preview your site:
```
(venv)$ heroku apps:create nurungram
(venv)$ git push heroku master
(venv)$ heroku open
```

9. From the web dashboard you can monitor and scale your app resources, enable add-ons like MongoDB, New Relic, etc.

	**https://dashboard.heroku.com/**


### 3. Routes & Templates ###

1. Routes in Flask are simple -- define a method and add a `route()` decorator. For example, in a blog-type app you might have a show_post() method that accepts a numeric post ID. The name of the method is not tied directly to the URI and the method can be re-used internally. Here's how that might look:

	```python
	@app.route('/post/<int:post_id>')
	def show_post(post_id):
	    # code to show the post with the given id, knowing the id is an integer
	```
	
2. You might also want to specify which HTTP methods a route responds to for RESTful apps. Here's an example of a route that might be part of a simple REST API for a blogging platform:

	```python
	@app.route('/api/v1/post', methods=['POST'])
	def add_post():
		# code to add blog post, given proper authentication
		# content-type must be of type 'application/json'
		if not request.json:
			# that ain't right
		blog_title = request.json['title']
	```


3. Templates in Flask utilize the widely used Jinja2 engine, which are modelled after Django's templates. They are straight forward, especially if you have any experience with Mustache, Handlebars, etc. I won't spend much time on them except to say that Flask expects them in the `templates` folder with an .html extension. It's easy to pass variables as keyword arguments to the `render_template()` method:

	```python
	@app.route('/hello/<name>')
	def hello(name):
	    return render_template('hello.html', name=name)
	```















