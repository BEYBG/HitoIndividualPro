from Productos import Producto
from Clientes import Cliente

class Pedido: #Pascal case
    def __init__(self, id, fecha_pedido, id_cliente, nombre_producto, unidades, coste_envio): #Constructor de clase
        self.id=id
        self.fecha_pedido=fecha_pedido
        self.id_cliente=id_cliente #snake_case
        self.nombre_producto=nombre_producto #snake_case
        self.unidades=unidades
        self.coste_envio=coste_envio
    def pagado():
        print('Se ha realizado el pedido, se ha procedido a enviar un correo con la factura')
    def enviarSMS(lista_productos): #camelCase
        if lista_productos:
            print('Seguimiento del pedido con los productos:')
            mostrarCompra()
            print('En tramite')
        else:
            print('No se puede hacer seguimiento del pedido, hable con atencion al cliente.')
    def facturar(self):
        print(f'Factura {self.id}.')
        print(f'Nombre de cliente {self.id_cliente}.')
        print(f'Unidades compradas {self.unidades}.')
    def costeEnvio(self): #camelCase
        if Cliente.mostrarPais() == 'España':
            coste_envio = Producto.mostrarPrecio() + 5
            print(f'El total con costes de envío es = {coste_envio}')
        else:
            coste_envio = Producto.mostrarPrecio() + 10
            print(f'El total con costes de envío es = {coste_envio}')
    def mostrarPedido(self): #camelCase
        print(f'Id: {self.id}\nFecha pedido: {self.fecha_pedido}\nId Cliente: {self.id_cliente}\nProducto: {self.nombre_producto}\nUnidades: {self.unidades}\nCoste_envío: {self.coste_envio}')








