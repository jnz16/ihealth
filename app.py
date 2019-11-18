#These modules are all from flask
from flask import Flask, render_template, request
#This module is from dotenv
from dotenv import load_dotenv
#These are python provided modules
import requests, os

app = Flask("BreastApp")

@app.route("/")
def home_page():
	return render_template("templates/index.html")

@app.route("/otherpage")
def other_page():
	return render_template("other_page.html")

@app.route("/userreport", methods=["GET", "POST"])
def user_name():
	#We use the request module to easily collect all the data input into the form
	form_data = request.form["name"]
	if request.form.get("swallen") == 'true' or request.form.get("lump") == 'true' or frequest.form.get("nipple") == 'true':
        return render_template("user_name.html", symptomresult=results, user_data=form_data)
    if request.form.get("swallen") == 'false' or request.form.get("lump") == 'false' or request.form.get("nipple") == 'false' and request.form.get("skin") == 'true' and request.form.get("pain") == 'true':  
        return render_template("wait48h.html", symptomresult=results, user_data=form_data)

app.run(debug=True)