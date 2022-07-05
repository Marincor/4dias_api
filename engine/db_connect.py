import os

from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL= os.getenv("DATABASE_URL")

engine = create_engine(f'{DATABASE_URL}', client_encoding='utf8', implicit_returning=True)

def register_new_company(company_name:str, web_site: str, source:str, approved: bool):
    with engine.connect() as conn:
        query = """ INSERT INTO companies (company_name, web_site, source, approved) VALUES (%s,%s,%s,%s)"""
        values = (company_name, web_site, source, approved)
        conn.execute(query,values)
        conn.close()
     
def find_company_by_name(company_name:str):
    with engine.connect() as conn:
        query = """ SELECT * FROM companies WHERE company_name = %s """
        values = (company_name)
        data = conn.execute(query,values)
        conn.close()
        return data.fetchone()
    

def approve_company_by_name(company_name:str, approved: bool):
    finded_company = find_company_by_name(company_name)
    if finded_company:
        with engine.connect() as conn:
            query = """ UPDATE companies SET approved = %s WHERE company_name = %s """
            values = (approved, company_name)
            conn.execute(query,values)
            conn.close()
        
        
def list_companies():
    with engine.connect() as conn:
        query = """ SELECT * FROM companies """
        data = conn.execute(query)
        conn.close()
        return data.fetchall()
 

def find_company_by_id(id:str):
    with engine.connect() as conn:
        query = """ SELECT * FROM companies WHERE id = %s """
        values = (id)
        data = conn.execute(query,values)
        conn.close()
        return data.fetchone() 
    