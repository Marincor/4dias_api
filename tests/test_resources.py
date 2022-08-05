import json
from app import app

def test_main():
    with app.test_client() as test_client:
        response = test_client.get("/");
        assert response.status_code == 200
        assert b"<!DOCTYPE html>" in  response.data
        
def test_create_company(): 
    new_company = {
        "company_name": "Company Test",
        "web_site": "https://companytest.com.br/",
        "source":"https://companyfont.com.br/"
    }
    with app.test_client() as test_client:
        response = test_client.post("/company", json=new_company);
        assert response.status_code == 201
           
def test_companies():
    with app.test_client() as test_client:
        response = test_client.get("/companies");
        assert response.status_code == 200
        assert b"company_name" in  response.data   
        
def test_company():        
     with app.test_client() as test_client:
        response = test_client.get("/company/1");
        assert response.status_code == 200
        assert b"company_name" in  response.data      
