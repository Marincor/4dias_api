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

@app.before_first_request
def connect_db():
     with engine.connect() as conn:
        with open("./migrations/companies.sql") as file:
            query = text(file.read())
            conn.execute(query) 
