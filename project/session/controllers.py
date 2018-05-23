from flask import session

def check_login_session():
    if 'email' in session:
        return True
    else:
        return False
