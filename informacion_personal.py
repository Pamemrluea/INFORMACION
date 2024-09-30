# UNIVERSIDAD ESTATAL AMAZONICA
#TAREA 15
#Pamela Morales
#Utilizar diccionarios en Python para representar información estructurada y realizar operaciones comunes.
#1 Crea un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Adela Pincay",
    "edad": 25,
    "ciudad": "Jipijapa",
    "profesion": "Licenciada de parvularia"
}

#2 Modificar el valor asociado a la clave "ciudad"
informacion_personal["ciudad"] = "Quito"

#3 Agregar una nueva clave-valor al diccionario que represente la nueva profesion
informacion_personal["nueva_profesion"] = "Ingeniera en contabilidad"

# Imprimir el diccionario modificado
print(informacion_personal)

#4 Verificar si la clave "telefono" existe en el diccionario, y si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0992635908"

# Imprimir el diccionario después de agregar el teléfono
print(informacion_personal)

#5 Eliminar la clave "edad" si existe
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
