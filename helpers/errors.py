server_error = {'message': 'An error ocurred while trying to save the information, please try again later!'}, 500
already_saved_error = {'message': 'This company is already registered'}, 400
required_fields_error = {'message': 'company_name and web_site are required fields'}, 400
company_not_found = {'message': 'Company not found!'}, 404

errors = {
    "server_error": server_error,
    "already_saved": already_saved_error,
    "required_fields": required_fields_error,
    "company_not_found": company_not_found
}