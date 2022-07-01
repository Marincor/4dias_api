
from flask import Blueprint


companies = Blueprint('companies', __name__);
company = Blueprint('company', __name__)

@companies.route("", methods=["GET"])
def list():
    return {'message': 'list of companies []'}, 200


@company.route("", methods=["GET", "POST"])
def search():
    return {'message': 'search company return'}, 200

def register_company():
    return {'message': 'teste' }