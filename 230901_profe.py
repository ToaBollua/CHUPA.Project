class persona:
    id = 0
    rut = ""
    nombre =""
    apellido_pa = ""
    apellido_ma = ""
    direccion =""
    celular = 0

    def __init__(self, id, rut, nombre, apellido_pa, apellido_ma, direccion,celular ):
        self.id = id
        self.rut = rut
        self.nombre = nombre
        self.apellido_pa = apellido_pa
        self.apellido_ma = apellido_ma
        self.direccion = direccion
        self.celular = celular


print("Id:",end="")
id = int(input() )
print("rut:",end="")
rut = input() 
print("nombre:",end="")
nombre = input() 
print("apellido_pa:",end="")
apellido_pa = input() 
print("apellido_ma:",end="")
apellido_ma = input() 
print("direccion:",end="")
direccion = input() 
print("celular:",end="")
celular = int(input() )

persona_1 = persona(id, rut, nombre, apellido_pa, apellido_ma, direccion, celular )

print("Contenido de la clase:")
print("Id:", persona_1.id)
print("rut:", persona_1.rut)
print("nombre:", persona_1.nombre)
print("apellido_pa:", persona_1.apellido_pa)
print("apellido_ma:", persona_1.apellido_ma)
print("direccion:", persona_1.direccion)
print("celular:", persona_1.celular)
    