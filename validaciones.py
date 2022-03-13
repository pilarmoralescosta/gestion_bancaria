import re


def validar_dni(dni):
    return re.fullmatch(r'^\d{8}(?:[-\s]\d{4})?$', dni)


def validar_cuit_cuil(cuit_cuil):
    return re.fullmatch(r'^(20|23|24|27|30|33|34)[0-9]{9}$', cuit_cuil)
