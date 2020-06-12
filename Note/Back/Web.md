# IO

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## Todo

- [ ] Read [paper](#paper-1)

## Reference

## Vision

- <IO>:
  - web I/Output and visualize Result
  - Contain : ML technology
  - []()

## Objective

### I/Output

#### Input

#### Example :

- In Cambridge Engineering Department. (STEM department)
  Speech recognition team.

- Total number of Chinese stuff
  Example :
  Cambridge factually number : What is the percentage of Chinese in there ? // STUB :
  Actual :

How to

## Flask simple

https://towardsdatascience.com/how-to-build-a-data-science-portfolio-website-335b0f253822
C:\Local\Work\ML_Name\web\web_dev\app.py

## Flask structure

### jinja

#### Template Inheritance

-[Source](https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/)

The most powerful part of Jinja is template inheritance.

1. layout.html is the “skeleton” :

- Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override.

2.  index.html is the t child templates

##### Example :

1. block :

- in layout.html
<title>{% block title %}{% endblock %}</title>
- in index.html :
- {% block title %}Welcome to Flask Tracking!{% endblock %}
  {% extends "layout.html" %}

  <the {% block %} tags define four blocks that child templates can fill in>

see : jinja2 snippets extension .

## Flask Personal task

### design

- add input box. in web page.
- visualization area : display the input text and simple pre-decided python plot

#### input box

- collect html snippets input : input box.

### min :

- [ ] create flask development git. : web_learn
- [ ]

### bare bone

ANCHOR bare bone

C:\Local\Work\Tools\web_learn : web_learn

#### How to run the

app.py
if **name** == "**main**":
app.run()
run as normal python file .

#### what is a boilerplat

C:\Local\Work\Tools\web_learn_boiler
functioning simple boilerplat :
run app.py in vscode

#### How insert a html in another HTML

{% block head %}

<title>{% block title %}{% endblock %} - My Webpage</title>
{% endblock %}

<div w3-include-html="cs_in_header.html"></div>

{% block head %}

<title>{% block title %}{% endblock %}</title>
{% endblock %}

#### How to use block as template

https://jinja.palletsprojects.com/en/2.11.x/templates/ -[Source](#https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/)
{% block footer %}Jim !{% endblock %}
{% block footer %}{% endblock %}

##### How

in layout.html : parent file

{% block head %}

<title> hi {% block title %}{% endblock %}</title>
{% endblock %}

in layout.html : child file
{% block title %}Welcome to My learning !{% endblock %}

##### Result

Welcome to My learning inserted into the title

#### How to verify the if server is working

run : C:\Local\Work\ML_Name\web\web_dev\app.py
is the boilerplat for the data scientist

#### How define form

https://medium.com/@mikaelagurney/add-dynamic-components-to-your-html-templates-using-form-s-flask-and-jinja-59b4169ec3e1


{% comment %} take in layout as parent template {% endcomment %}
{% extends "layout_v1.html" %}
{% import "helpers/forms.html" as forms %}
{% block title %}Welcome to My learning !{% endblock %}
{% block footer %} Jim !{% endblock %}

<h1>{{ self.title() }}</h1>

    {% comment %} form   {% endcomment %}

<form action="/site" method="POST">
<fieldset>
<legend>Add A Site</legend>
{{ forms.render(site_form) }}
<p><input type="Submit" value="Save Site"></p>
</fieldset>
</form>

## Reading

### Middle size App development : Python Web Applications with Flask – Part I

- [Python Web Applications with Flask – Part I](https://realpython.com/python-web-applications-with-flask-part-i/)

- [ ] read though and implement part I.
- [ ] modularize import ones , and build own part .

#### Other note

- install yellow mark out. : yellow highlighter pen for web
  - [yellow highlighter](https://chrome.google.com/webstore/detail/yellow-highlighter-pen-fo/lnmengjdnfjbochkdkcjbbpildacancp)
- [ ] covert copy 2 lines into the ssmrco

#### Why demo:

- The focus that building an application rather than a boilerplate
- in this tutorial series we are going to be building a **mid-sized application** of our own and as a side-effect generating a boilerplate.
- The hope is that when we are finished we will have a better appreciation for what Flask provides and what we can build around it.

#### What we are building

goal
tracking visits to a site

##### Spec :

- Register with the application.
- Add sites to their account.
- Install tracking codes on their site(s) to track various events as the events occur.
- View reports on their site(s)’ event activity.

##### Learnt

- Learn how to develop a mid-sized application using Flask.
- Get practical experience with refactoring and testing.
- Gain a deeper appreciation of building composable systems.
- Develop a boilerplate that we can re-use for future projects.

#### Test Run :

Python 3.8 : make small modification :

- add Werkzeug==0.16.1 to requirements.txt
- modified time.clock to time.process_time
- run in vscode environement
- website :
  http://127.0.0.1:5000/

#### Dependencies

We will start with dependencies on three libraries -
Flask itself for managing the request / response cycle,
Flask-WTF for its CSRF protection and data validation and finally
Flask-SQLAlchemy for **database** connection pooling and object / relational mapper.
Here is our **requirements.txt** file:

#### File structure

├── flask-tracking.db
├── requirements.txt
├── templates
│ ├── data_list.html
│ ├── helpers
│ │ ├── forms.html
│ │ └── tables.html
│ ├── index.html
│ ├── layout.html
│ └── validation_error.html
└── tracking.py

#### HTML view

see jinja : and  
Template Inheritance

https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/

### Flask Boilerplate

- [ ] Read and understand drop down menue
      Boilerplate template for a Python Flask application with Flask-SQLAlchemy, Flask-WTF, Fabric, Coverage, and Bootstrap http://www.flaskboilerplate.com

- [Boilerplate](https://github.com/realpython/flask-boilerplate.git)

### How to Build a Data Science Portfolio Website

C:\Local\Work\ML_Name\web\web_dev\app.py

#### Objective

guide that will hopefully help you create your own data science portfolio website

#### web framework : flask

install flask : pip install flask
try \$env:FLASK_APP = "app.py"
run : python -m flask run

#### web framework : flask

60 min
[Django vs. Flask in 2019: Which Framework to Choose](https://testdriven.io/blog/django-vs-flask/)
Regardless of whether your end goal is to learn Flask or Django, start with Flask. It's a great tool for learning web development fundamentals and best practices along with the core pieces of a web framework that are common to almost all frameworks.

###

https://realpython.com/python-web-applications-with-flask-part-i/

pip install -r .\requirements.txt

## Reference

- [How to Build a Data Science Portfolio Website](https://towardsdatascience.com/how-to-build-a-data-science-portfolio-website-335b0f253822)

- [What is Flask Python](https://pythonbasics.org/what-is-flask-python/)
