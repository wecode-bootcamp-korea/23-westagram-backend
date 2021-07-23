import re

def email_validation(email):
    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[.]?\w{2,3}$'
    return re.search(email_regex, email)

def password_validation(password):
    passeord_regex = '[A-Za-z0-9!@##$%^&+=]{8,25}'
    return re.search(passeord_regex, password)  