import re


def validar_dni(dni):
    if re.search('^\d{8}(?:[-\s]\d{4})?$', dni):
        return True
    else:
        return False


def validar_cuit_cuil(cuit_cuil):
    if re.search('\b(20|23|24|27|30|33|34)(\D)?[0-9]{8}(\D)?[0-9]', cuit_cuil):
        return True
    else:
        return False
