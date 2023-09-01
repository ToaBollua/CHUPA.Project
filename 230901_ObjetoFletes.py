class persona:
    id = 0
    nombre = ""
    apellido_paterno = ""
    apellido_materno = ""
    direccion = ""
    email = ""
    rut = ""
    telefono_contacto = ""
    
    def __init__(self, id, rut, nombre, apellido_paterno, apellido_materno, direccion, email, rut, telefono_contacto):
        self.id = id
        self.rut = rut
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.direccion = direccion
        self.email = email
        self.telefono_contacto = telefono_contacto

class cliente:
    fecha_pedido = ""
    fecha_envio = ""
    fecha_entrega = ""
    tarifa = 0
    fecha_pago = ""
        

class cliente_empresa:
    fecha_pedido = ""
    fecha_envio = ""
    fecha_entrega = ""
    tarifa = 0
    rut_empresa = ""
    giro = ""
    razon_social = ""
    

class chambeadores:
    cargo = ""
    fecha_de_incorporación = ""
    remuneración = 0
    jornada = ""
    
    
class vehiculo:
    id = 0
    patente = ""
    tipo = ""
    permiso_circulacion = False
    revision_tecnica = False
    fecha_revision_tec = ""

class contabilidad:
    id = 0
    fecha = ""
    activo = 0
    pasivo = 0