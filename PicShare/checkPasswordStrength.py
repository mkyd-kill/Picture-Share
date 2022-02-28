def passwordStrength(password) -> str:
    from re import compile, search
    from flask import flash
    """
        Password Strength must have:
            # Atleast one number
            # Atleast one uppercase & lowercase letter
            # Atleast one special symbol
            # Should be 8 <= password <= 20 long
    """
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pssword = ""

    # compile the regex experssions
    password_checker = compile(regex)

    # search for the regex in the password
    password_match = search(password_checker, password)

    if len(password) < 8:
        flash("Make sure your password is at least 8 characters long", category='error')
    elif not password_match:
        flash("Make Sure Password Has: one number, one uppercase and lowercase letter and one special symbol", category='error')
    else:
        pssword = password
    
    return pssword