def approve_email_html(company_name:str, link: str): 
   return """
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <div style="width: 80%; margin: 0 auto; margin-bottom: 10px">
      <h1 style="color: rgb(140, 82, 255); font-family: sans-serif">
        Olá, Admin, existe uma nova empresa aguardando sua aprovação!
      </h1>
      <h2 style="color: darkgray; font-family: sans-serif">
        Aprovar a empresa {} ?
      </h2>
      <div> 
         <a
        style="padding:10px 80px; background:rgb(140,82,255); color:white; text-decoration:none;display: block;text-align: center;"
        href="{}"
      >
        Aprovar
      </a>
      </div>
      <img
        src="https://i.ibb.co/P1sxbxr/4dias-logo.png"
        alt="4 dias - logo"
        title="4 dias"
      />
    </div>
  </body>
</html>
    """.format(company_name, link)
    
    
def dict_to_json_company(raw_company):
  company =  {
        "id": raw_company['id'],
        "company_name": raw_company['company_name'],
        "web_site": raw_company['web_site'],
        "source": raw_company['source']
    }
  return company