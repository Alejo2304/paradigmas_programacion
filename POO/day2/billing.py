class Persona:

    def __init__(self):
        self.codigo = 0
        self.nombre = ""
        self.telefono = ""
        self.email = ""
        self.credito = 0.0

    def setCodigo(self, cod): #update self.codigo
        self.codigo = cod

    def getCodigo(self): #return the value of self.codigo
        return self.codigo 

    def setNombre(self, name): #update self.codigo
        self.nombre = name

    def getNombre(self): #return the value of self.codigo
        return self.nombre 
    
    def setTelefono(self, tel): #update self.codigo
        self.telefono = tel

    def getTelefono(self): #return the value of self.codigo
        return self.telefono 
    
    def setEmail(self, ema): #update self.codigo
        self.email = ema

    def getEmail(self): #return the value of self.codigo
        return self.email 
    
class Cliente(Persona): 
    
    def __init__(self):
        self.credito = 0.0

    def setCredito(self, credit):
        self.credito = credit

    def getCredito(self): #return the value of self.codigo
        return self.credito 
    
class Vendedor(Persona):
    def __init__(self):
       self.direccion

    def setDireccion(self, address): #update self.codigo
        self.direccion = address

    def getDireccion(self):
        return self.direccion


class Producto:
    def __init__(self):
        pass

class Factura:
    def __init__(self):
        pass


cliente1 = Cliente() #Instanciar una clase. 
