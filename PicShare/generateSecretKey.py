# This will randomly generate a secret key everytime the app is initialised
def secretKey() -> str:
    from string import ascii_letters, digits, punctuation
    from re import search
    from random import choice
    import secrets
    from uuid import uuid4
    for num in range(1, 20):
        if num < 15:
            pass
        else:
            alphanumerics = ascii_letters + digits + punctuation
            scr = "".join(choice(alphanumerics) for _ in range(num))
            if search(r'(.)\1\1', scr) and search(r'(..)(.*?)\1', scr):
                secretKey()
            else:
                return scr + str(secrets.token_hex(26)) + str(uuid4().hex)