# Import the flask package to be used in the application
from flask import Flask 
from flask import render_template
from flask import url_for
from flask import request

# initialize the flask application as an App
app = Flask(__name__)

#create a route to be rendered in the webPage
@app.route('/')

#define a function that would trigger the home url
#to be redirected to the rendered view

def homepage():
	return render_template('home.html')

#create an error handler page to tell the app
#to redirect to that page in event of an err
@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404

#run the application main Loop for event to be
#carried out explictly
if __name__ == '__main__':
	app.run(debug=True)
