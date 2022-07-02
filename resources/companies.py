
from flask import Blueprint, request
from engine.db_connect import find_company_by_name, register_new_company
from helpers.errors import errors

companies = Blueprint('companies', __name__);
company = Blueprint('company', __name__)

@companies.route("", methods=["GET"])
def list():
    return {'message': 'list of companies []'}, 200


@company.route("", methods=["POST"])
def register_company():
    data = request.json
    
    if 'company_name' not in data or 'web_site' not in data:
        return errors["required_fields"]
    
    company_name = data['company_name']
    web_site = ''
    source = ''
    approved = False
    
    if 'web_site' in data:
        web_site = 'web_site'
    if 'source' in data:
        source = data['source']  
     
    try:
        already_registered = find_company_by_name(company_name)
    except:
        return errors["server_error"]  
    
    if already_registered:
        return errors["already_saved"]  
    
    try:
        register_new_company(company_name, web_site, source, approved)
    except:
        return errors["server_error"]   
    
    return {'message': 'company successfully created!' }, 201