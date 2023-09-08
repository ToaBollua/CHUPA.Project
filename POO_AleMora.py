class persona:
    id = 0
    rut = ""
    nombre = ""
    a_materno = ""
    a_paterno = ""
    direccion = ""
    numero_contacto = 0

    def __init__(self, id, rut, nombre, a_materno, a_paterno, direccion, numero_contacto):
        self.id = id
        self.rut = rut 
        #seguir con las demás variables#
        

class trabajadores:
    id = 0
    celular = 0
    cargo = ""
    fecha_incorporacion = ""
    remuneracion = 0
    jornada = ""

class cliente:
    id = 0
    rut_empresa = ""
    razon_social = ""
    giro = ""
    numero_envio = 0
    fecha_pedido = ""
    fecha_envio  = ""
    fecha_entrega = ""
    tarifa = ""

class carga:
    id = 0
    lugar_origen = ""
    lugar_destino = ""
    peso = 0
    volumen = 0

class vehiculo:
    id = 0
    patente = ""
    tipo = ""
    permiso_circulacion = bool
    revision_tecnica = bool
    fecha_revision_tecnica = ""

class contabilidad:
    id = 0
    fecha = ""
    activo = 0
    pasivo = 0