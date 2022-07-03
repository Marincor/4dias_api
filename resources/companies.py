
import json
from flask import Blueprint, jsonify, make_response, render_template, request
from flask_jwt_extended import create_access_token, jwt_required
from engine.db_connect import find_company_by_id, find_company_by_name, list_companies, register_new_company, approve_company_by_name
from helpers.errors import errors
from helpers.mailgun import send_approve_email
from helpers.utils import dict_to_json_company

companies = Blueprint('companies', __name__);
company = Blueprint('company', __name__)

@companies.route("", methods=["GET"])
def list():
    companies = list_companies()
    
    return jsonify({'result': [dict(row) for row in companies]}), 200


@company.route("/<id>", methods=["GET"])
def show_company_by_id(id):
    try:
        finded_company = find_company_by_id(id)
    except:
        return errors["server_error"]    
    if finded_company:
        company = dict_to_json_company(finded_company)
        return {'result': company}, 200
    return errors["company_not_found"] 


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
        web_site = data['web_site']
    if 'source' in data:
        source = data['source']  
     
    try:
        already_registered = find_company_by_name(company_name);
    except:
        return errors["server_error"]  
    
    if already_registered:
        return errors["already_saved"]  
    
    try:
        register_new_company(company_name, web_site, source, approved)
    except:
        return errors["server_error"]   
    
    create_token = create_access_token(identity=company_name)
    access_token = jsonify(access_token=create_token).json['access_token']
    
    try:
        send_approve_email(company_name, access_token)
    except:
        return errors["server_error"]      
    return {'message': 'company successfully created!' }, 201


@company.route("/approve-register",methods=["GET"])
@jwt_required()
def approve_register():
    company_name = request.args.get("company_name")
    approved = request.args.get("approved") == "true"
    
    try:
        company_exist = find_company_by_name(company_name)
    except:
        return errors["server_error"]   
    
    if company_exist is None:
        return errors["company_not_found"] 
    
    if approved:
        try:
            approve_company_by_name(company_name, approved)
        except:
            return errors["server_error"]    
        return make_response(render_template("approved_message.html")), 200
    
    return errors["server_error"] 