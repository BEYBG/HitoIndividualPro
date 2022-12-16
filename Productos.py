

class Producto: #Pascal case
    def __init__(self, id_producto, nombre_producto, categoria, unitstock, precio, fecha_fabricacion): #Constructor de clase
        self.id_producto=id_producto #snake_case
        self.nombre_producto=nombre_producto #snake_case
        self.categoria=categoria
        self.unitstock=unitstock
        self.precio=precio
        self.fecha_fabricacion=fecha_fabricacion #snake_case
    def reponerStock (self): #camelCase / Método para reponer stock
        if self.unitstock <12:
            print(f'El stock es ahora de {self.unitstock}')
            self.unitstock+=20
            print(f'Pedidas 20 unidades.El nuevo stock es de {self.unitstock} unidades')
        else:
            print(f'el stock actual es {self.unitstock}')
    def mostrarProducto (self): #camelCase / Método para mostrar datos de un producto
        print(f'Información del Producto:\n')
        print(f'Nombre: {self.nombre_producto} Precio: {self.precio}')
    def mostrarPrecio (self): #camelCase /Método para mostrar el precio del producto (usarlo en otra función para hacer cálculos)
        print(int(self.precio))





