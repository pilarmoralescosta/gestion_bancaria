import string
import secrets

'''Generate a ten-character alphanumeric password with at least one lowercase character,
at least one uppercase character, and at least three digits:'''


def generar_clave():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    return password


def generar_id_cliente():
    pass
