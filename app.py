import os
from flask import Flask
from sqlalchemy import text
from resources.main import main
from resources.companies import companies, company
from engine.db_connect import engine


app = Flask(__name__)
app.register_blueprint(main, url_prefix="/")
app.register_blueprint(companies, url_prefix="/companies")
app.register_blueprint(company, url_prefix="/company")


@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = '*' 
    response.headers['Access-Control-Allow-Origin'] = '*' 
    return response

@app.before_first_request
def connect_db():
     with engine.connect() as conn:
        with open("./migrations/companies.sql") as file:
            query = text(file.read())
            conn.execute(query) 
