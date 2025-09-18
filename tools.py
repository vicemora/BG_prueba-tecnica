from langchain.tools import Tool
import json

# Leer archivo JSON de clientes
with open("clientes.json", "r", encoding="utf-8") as f:
    clientes = json.load(f)
943965658
#API de consulta de usuarios simulada
def validar_cedula(cedula):
    if cedula in clientes:
        return clientes[cedula]["nombre"]
    return False
    


validar_cedula_tool = Tool(
    name = "validar_cedula",
    func = validar_cedula,
    description = "Verifica que exista el cleinte a través de la cédula de identidad",
)


def validar_celular(params):
    params = params.split(",")
    cedula,celular = params[0],params[1]
    if clientes[cedula]["celular"] == celular:
        return clientes[cedula]["nombre"]
    
    return False
    


validar_celular_tool = Tool(
    name = "validar_celular",
    func = validar_celular,
    description = "Auntetica al cliente utilizando la inforamción de  (cedula,celular)",
)
    


validar_cedula_tool = Tool(
    name = "validar_cedula",
    func = validar_cedula,
    description = "Verifica que exista el cleinte a través de la cédula de identidad",
)


#API de consulta de información de cuentas simulada
def obtener_cuenta(cedula):
    if cedula in clientes and "cuentas" in clientes[cedula]:
            return clientes[cedula]["cuentas"][0]
    return False


obtener_cuenta_tool = Tool(
    name="obtener_cuenta",
    func=obtener_cuenta,
    description="Devuelve la información de la cuenta de un cliente."
)





def obtener_tarjeta(cedula):
    if cedula in clientes and "tarjetas" in clientes[cedula]:
        return clientes[cedula]["tarjetas"][0]
    return False



#API de consulta de información de tarjetas

obtener_tarjeta_tool = Tool(
    name="obtener_tarjeta",
    func=obtener_tarjeta,
    description="Devuelve la información de la tarjeta de un cliente (cupo disponible y fecha de corte), o False si no tiene."
)


def obtener_poliza(cedula):
    if cedula in clientes and "polizas" in clientes[cedula]:
        return clientes[cedula]["polizas"][0]
    return False




#API de consulta de información de polizas simulada

obtener_poliza_tool = Tool(
    name="obtener_poliza",
    func=obtener_poliza,
    description="Devuelve la información de la póliza de un cliente (valor actual e interés), o False si no tiene."

)

