class Cliente: 
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
    
    def setCredito(self, credito): #update self.codigo
        self.credito = credito

    def getCredito(self): #return the value of self.codigo
        return self.credito 
    
class Vendedor:
    def __init__(self):
        self.codigo = 0
        self.nombre = ""
        self.telefono = ""
        self.email = ""
        self.direccion = ""

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
    
    def setCredito(self, address): #update self.codigo
        self.direccion = address

    def getCredito(self): #return the value of self.codigo
        return self.direccion 

class Producto:
    def __init__(self):
        pass

class Factura:
    def __init__(self):
        pass


cliente1 = Cliente() #Instanciar una clase. 
