import datetime

class persona:
    id = 0
    rut = ""
    nombre = ""
    a_materno = ""
    a_paterno = ""
    direccion = ""
    numero_contacto = 0
    fecha_nacimiento = ""

    def __init__(self, id, rut, nombre, a_materno, a_paterno, direccion, numero_contacto, fecha_nacimiento):
        self.id = id
        self.rut = rut 
        self.nombre = nombre
        self.a_materno = a_materno
        self.a_paterno = a_paterno
        self.direccion = direccion
        self.numero_contacto = numero_contacto
        self.fecha_nacimiento = fecha_nacimiento
    
    def __del__(self):
        id = 0
        rut = ""
        nombre = ""
        a_materno = ""
        a_paterno = ""
        direccion = ""
        numero_contacto = 0
        fecha_nacimiento = ""
        
    #   CONTINUAR AQUI
    def calcula_edad(self):
        pass
    
        

class trabajadores:
    id = 0
    celular = 0
    cargo = ""
    fecha_incorporacion = ""
    remuneracion = 0
    jornada = ""
    licencia_vigente = bool

    def __init__(self, id, celular, cargo, fecha_incorporacion, remuneracion, jornada, licencia_vigente):
        self.id = id
        self.celular = celular
        self.cargo = cargo
        self.fecha_incorporacion = fecha_incorporacion
        self.remuneracion = remuneracion
        self.jornada = jornada
        self.licencia_vigente = licencia_vigente
    
    def __del__(self):
        id = 0
        celular = 0
        cargo = ""
        fecha_incorporacion = ""
        remuneracion = 0
        jornada = ""
        licencia_vigente = bool
        
        
class cliente:
    id = 0
    numero_envio = 0
    
    def __init__(self, numero_envio, fecha_pedido, fecha_envio, fecha_entrega, tarifa):
        self.id = id
        self.numero_envio = numero_envio
    
    def __del__(self):
        id = 0
        numero_envio = 0
        

class carga:
    id = 0
    lugar_origen = ""
    lugar_destino = ""
    peso = 0
    volumen = 0
    
    def __init__(self, id, lugar_origen, lugar_destino, peso, volumen):
        self.id = id
        self.lugar_origen = lugar_origen
        self.lugar_destino = lugar_destino
        self.peso = peso
        self.volumen = volumen
    
    def __del__(self):
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
    
    def __init__(self, id, patente, tipo, permiso_circulacion, revision_tecnica, fecha_revision_tecnica):
        self.id = id
        self.patente = patente
        self.tipo = tipo
        self.permiso_circulacion = permiso_circulacion
        self.revision_tecnica = revision_tecnica
        self.fecha_revision_tecnica = fecha_revision_tecnica
        
    def __del__(self):
        id = 0
        patente = ""
        tipo = ""
        permiso_circulacion = bool
        revision_tecnica = bool
        fecha_revision_tecnica = ""
        

class transacciones:
    id = 0
    fecha = ""
    activo = 0
    pasivo = 0
    fecha_pedido = ""
    fecha_envio  = ""
    fecha_entrega = ""
    pago = ""
    
    def __init__(self, id, fecha, activo, pasivo):
        self.id = id
        self.fecha = fecha
        self.activo = activo
        self.pasivo = pasivo
        
    def __del__(self):
        id = 0
        fecha = ""
        activo = 0
        pasivo = 0
        
class empresa:
    id = 0
    giro = ""
    razon_social = ""
    tipo_empresa = ""
    correo_empresarial = ""
    rut_empresa = ""
    #   CONTINUAR AQUI (?)

    def __init__(self, id, giro, razon_social, tipo_empresa, correo_empresarial, rut_empresa):
        self.id = id
        self.giro = giro
        self.razon_social = razon_social
        self.tipo_empresa = tipo_empresa
        self.correo_empresarial = correo_empresarial
        self.rut_empresa = rut_empresa
    
    def __del__(self):
        id = 0
        giro = ""
        razon_social = ""
        tipo_empresa = ""
        correo_empresarial = ""
        rut_empresa = ""
        

class inventario:
    conductor = ""
    tipo_vehiculo = ""
    disponibilidad_vehiculo = 0
#   CONTINUAR AQUI
    
    def __init__(self, conductor, tipo_vehiculo, disponibilidad_vehiculo):
        self.conductor = conductor
        self.tipo_vehiculo = tipo_vehiculo
        self.disponibilidad_vehiculo = disponibilidad_vehiculo
        
    def __del__(self):
        conductor = ""
        tipo_vehiculo = ""
        disponibilidad_vehiculo = 0