def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_especial = False
    caracteres_especiales = "!@#$%^&*"

    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        elif caracter in caracteres_especiales:
            tiene_caracter_especial = True

    return (tiene_mayuscula and tiene_minuscula and
            tiene_numero and tiene_caracter_especial)

contraseña = input("Introduce la contraseña a validar: ")
if validar_contraseña(contraseña):
    print("La contraseña es válida.")
else:
    print("La contraseña no cumple con los criterios.")
