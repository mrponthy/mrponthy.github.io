from flask import Flask, render_template
import sqlite3
import csv
app = Flask(__name__)

######################
## Define functions ##
######################
def read_db(query):
	conn = sqlite3.connect('Portfolio.db')
	c = conn.cursor()
	c.execute(query)
	return c.fetchall()

############################
## Get list of categories ##
############################
q = """ SELECT DISTINCT category FROM projects """
lijst = []
for element in read_db(q):
	lijst.append(str(element[0].encode('ascii')).title())

##################
## Create pages ##
##################
@app.route('/')
def page_home():
	return render_template("home.html", categorylist=lijst)

@app.route('/about/')
def page_about():
	return render_template("about.html", categorylist=lijst)

@app.route('/projects/<name>/')
def page_projects(name):
	lijstje = read_db(""" SELECT * FROM projects where category = '%s' """ % (name.lower()))
	try:
		return render_template("projectmodel.html", name=name, contentlist=lijstje, categorylist=lijst)
	except FileNotFoundError:
		return render_template("error.html", categorylist=lijst)

@app.route('/contact/')
def page_contact():
	return render_template("contact.html", categorylist=lijst)

@app.errorhandler(404)
def page_not_found(e):
	return render_template("error.html", categorylist=lijst), 404

if __name__ == '__main__':
	app.debug = True
	app.run()
