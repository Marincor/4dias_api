from dotenv import load_dotenv
from flask import request
import requests
import os

from helpers.utils import approve_email_html

load_dotenv()

MAILGUN_API_DOMAIN = os.getenv('MAILGUN_API_DOMAIN')
MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
FROM_TITLE_PERSON = os.getenv('FROM_TITLE_PERSON')
FROM_EMAIL =  os.getenv('FROM_EMAIL')
APPROVER_EMAIL =  os.getenv('APPROVER_EMAIL')
APPROVER_EMAIL_SUBJECT = os.getenv('APPROVER_EMAIL_SUBJECT')

def send_email(company_name: str, link:str):
      url = f"https://api.mailgun.net/v3/{MAILGUN_API_DOMAIN}/messages"
      html =  approve_email_html(company_name, link)
      res = requests.post(url, auth=('api', MAILGUN_API_KEY), 
                    data={'from': f'{FROM_TITLE_PERSON} <{FROM_EMAIL}>', 
                          'to': APPROVER_EMAIL, 
                          'subject': APPROVER_EMAIL_SUBJECT,
                          'text': f"Please confirm your company register clicking in the link: {link}",
                          'html': html}
        )
      return res
   
            
            
def send_approve_email(company_name:str, access_token:str):
    host = request.url_root[:-1]
    endpoint = "/company/approve-register"
    query_params = f'?company_name={company_name}&approved=true&jwt={access_token}'
    link =  host + endpoint + query_params
    res = send_email(company_name,link)
    return res
   