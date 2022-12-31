from flask import render_template, url_for, flash, redirect
from ResumeParser import app
from ResumeParser.parserMain import *

@app.route("/")
@app.route("/home")
def home():
    data = parser('ResumeParser/resumes/33.pdf')
    name = data["name"]
    email = data["email"]
    mobile_number = data["mobile_number"]
    skills = data["skills"]
    college_name = data["college_name"]
    degree = data["degree"]
    designation = data["designation"]
    return render_template(
        'home.html', 
        name=name,
        email = email,
        mobile_number = mobile_number,
        skills = skills,
        college_name = college_name,
        degree = degree,
        designation = designation
        )

@app.route("/")
@app.route("/extracter")
def extractor():
    return render_template()
