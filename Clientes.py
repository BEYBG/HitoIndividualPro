
class Cliente: #Pascal Case
    def __init__(self, id_cliente, nombre_cliente, apellidos, domicilio, poblacion, provincia, cp, pais, telefono, mail): #Constructor
        self.id_cliente=id_cliente #snake_case
        self.nombre_cliente=nombre_cliente #snake_case
        self.apellidos=apellidos
        self.domicilio=domicilio
        self.poblacion=poblacion
        self.provincia=provincia
        self.cp=cp
        self.pais=pais
        self.telefono=telefono
        self.mail=mail
    def mostrarCliente(self): #método para mostrar datos del cliente #camelCase
        print(f'Nombre: {self.nombre_cliente}\nApellidos: {self.apellidos}\nDomicilio: {self.domicilio}\nPoblación: {self.poblacion}\nProvincia: '
              f'{self.provincia}\nCP: {self.cp}\nPaís: {self.pais}\nTeléfono: {self.telefono}\nMail: {self.mail}')
    def mostrarPais(self): #método para extraer el dato de país del cliente #camelCase
        print(self.pais)












