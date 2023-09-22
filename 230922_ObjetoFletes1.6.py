class Persona:
    id_persona = 0
    rut = ""
    nombre = ""
    a_materno = ""
    a_paterno = ""
    direccion = ""
    numero_contacto = 0
    fecha_nacimiento = ""

    def __init__(self, id_persona, rut, nombre, a_materno, a_paterno, direccion, numero_contacto, fecha_nacimiento):
        self.id_persona = id_persona
        self.rut = rut 
        self.nombre = nombre
        self.a_materno = a_materno
        self.a_paterno = a_paterno
        self.direccion = direccion
        self.numero_contacto = numero_contacto
        self.fecha_nacimiento = fecha_nacimiento
    
    def __del__(self):
        self.id = 0
        self.rut = ""
        self.nombre = ""
        self.a_materno = ""
        self.a_paterno = ""
        self.direccion = ""
        self.numero_contacto = 0
        self.fecha_nacimiento = ""
        

    def calcula_edad(self):
        pass
    
        

class Trabajador(Persona):
    id_trabajador = 0
    celular = 0
    cargo = ""
    fecha_incorporacion = ""
    remuneracion = 0
    jornada = ""
    licencia_vigente = False

    def __init__(self, id_trabajador, celular, cargo, fecha_incorporacion, remuneracion, jornada, licencia_vigente,id_persona, rut, nombre, a_materno, a_paterno, direccion, numero_contacto, fecha_nacimiento):
        self.id_trabajador = id
        self.celular = celular
        self.cargo = cargo
        self.fecha_incorporacion = fecha_incorporacion
        self.remuneracion = remuneracion
        self.jornada = jornada
        self.licencia_vigente = licencia_vigente
        super().__init__(id_persona, rut, nombre, a_materno, a_paterno, direccion, numero_contacto, fecha_nacimiento)
    
    def __del__(self):
        self.id = 0
        self.celular = 0
        self.cargo = ""
        self.fecha_incorporacion = ""
        self.remuneracion = 0
        self.jornada = ""
        self.licencia_vigente = False

    def tiene_licencia(self):
        self.licencia_vigente = True

        
        
class Cliente(Persona):
    id_cliente = 0
    numero_envio = 0
    
    def __init__(self,id_cliente, numero_envio, fecha_pedido, fecha_envio, fecha_entrega, tarifa, id_persona, rut, nombre, a_materno, a_paterno, direccion, numero_contacto, fecha_nacimiento):
        self.id = id
        self.numero_envio = numero_envio
        super().__init__(id_persona, rut, nombre, a_materno, a_paterno, direccion, numero_contacto, fecha_nacimiento)
    def __del__(self):
        self.id = 0
        self.numero_envio = 0
        

class Carga:
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
        self.id = 0
        self.lugar_origen = ""
        self.lugar_destino = ""
        self.peso = 0
        self.volumen = 0
        

class Vehiculo:
    id = 0
    patente = ""
    tipo = ""
    permiso_circulacion = False
    revision_tecnica = False
    fecha_revision_tecnica = ""
    
    def __init__(self, id, patente, tipo, permiso_circulacion, revision_tecnica, fecha_revision_tecnica):
        self.id = id
        self.patente = patente
        self.tipo = tipo
        self.permiso_circulacion = permiso_circulacion
        self.revision_tecnica = revision_tecnica
        self.fecha_revision_tecnica = fecha_revision_tecnica
        
    def __del__(self):
        self.id = 0
        self.patente = ""
        self.tipo = ""
        self.permiso_circulacion =  False
        self.revision_tecnica = False
        self.fecha_revision_tecnica = ""

    def tiene_permiso(self):
        self.permiso_circulacion = True

    def revision_al_dia(self):
        self.revision_tecnica = True


class Empresa(Cliente):
    id_cliente = 0
    giro = ""
    razon_social = ""
    tipo_empresa = ""
    correo_empresarial = ""
    rut_empresa = ""

    def __init__(self, id_cliente, giro, razon_social, tipo_empresa, correo_empresarial, rut_empresa):
        self.cliente_id = id
        self.giro = giro
        self.razon_social = razon_social
        self.tipo_empresa = tipo_empresa
        self.correo_empresarial = correo_empresarial
        self.rut_empresa = rut_empresa
    
    def __del__(self):
        self.cliente_id = 0
        self.giro = ""
        self.razon_social = ""
        self.tipo_empresa = ""
        self.correo_empresarial = ""
        self.rut_empresa = ""
        

class Disponibilidad:
    cantidad_conductores = 0
    cantidad_vehiculos = 0
    disponibilidad_vehiculo = 0

    def __init__(self, cantidad_conductores, cantidad_vehiculos, disponibilidad_vehiculo):
        self.conductor = conductor
        self.tipo_vehiculo = tipo_vehiculo
        self.disponibilidad_vehiculo = disponibilidad_vehiculo
        
    def __del__(self):
        self.cantidad_conductores = 0
        self.cantidad_vehiculos = 0
        self.disponibilidad_vehiculo = 0
    
    def agregar_conductor(self):
            self.cantidad_conductores +=1
            return

    def agregar_vehiculos(self):
            self.cantidad_vehiculos +=1
            return

class InformacionEnvio:
    id = 0
    fecha_pedido = ""
    fecha_envio = ""
    fecha_entrega = ""
    pago = 0
    carga =  Carga()
    conductor = Trabajador()
    vehiculo = Vehiculo()

    def __init__(self, fecha_pedido, fecha_envio, fecha_entrega, pago, carga, conductor, vehiculo):
        self.id = id
        self.fecha_pedido = ""
        self.fecha_envio = ""
        self.pago = 0
        self.conductor = Trabajador()
        self.vehiculo = Vehiculo()
        self.carga = Carga()

    def __del__(self):
        self.id = id
        self.fecha_pedido = ""
        self.fecha_envio = ""
        self.pago = 0
        self.conductor = None
        self.vehiculo = None
        self.carga = None

class RegistroEnvio:
    info_envio = InformacionEnvio()

    def __init__(self, info_envio):
        self.info_envio = InformacionEnvio()

    def __del__(self):
        self.info_envio = None

    def registrar_datos():
        pass
