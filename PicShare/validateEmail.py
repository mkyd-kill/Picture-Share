def validEmail(email):
    from re import fullmatch
    from flask import flash
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    valid_email = ""
    if (fullmatch(regex, email)):
        valid_email = email
    else:
        flash("Invalid Email Address. Try Again...", category='error')
    return valid_email