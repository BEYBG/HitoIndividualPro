from Pedidos import Pedido
from Productos import Producto
from Clientes import Cliente

cliente1 = Cliente(234, 'Paula', 'García Pérez', 'c/Motril 6,4ºC', 'Arroyomolinos', 'Madrid', '123', 'España', '639',
                   'pau@gmail.com')
cliente2 = Cliente(235, 'Marcos', 'de la Vega Rodríguez', 'c/barcelona 45, 3ºA', 'Móstoles', 'Madrid', '234', 'España',
                   '688', 'marc@gmail.com')
cliente3 = Cliente(236, 'Jorge', 'Ruíz Ibarra', 'c/Ibiza 7, 2ºB', 'Fuenlabrada', 'Madrid', '345', 'España', '647',
                   'jorge@gmail.com')

Producto1 = Producto(2540, 'Funko Joker', 'figuras', 23, 20.95, '12/03/2020')
Producto2 = Producto(2300, 'BSO El Señor de los Anillos', 'música', 11, 9.99, '23/05/2011')
Producto3 = Producto(1380, 'Agenda 2023 Cactus', 'papelería', 13, 14.95, '15/09/2022')
Producto4 = Producto(1623, 'Posavasos Star Wars', 'decoracion', 10, 4.50, '28/02/2021')
Producto5 = Producto(1988, 'Funko Harley Queen', 'figuras', 14, 20.95, '4/07/2020')

Pedido1 = Pedido(678, '14/11/2022', 234, 'Funko Joker', 1, 'Envío Nacional=5 - Envío internacional=10')
Pedido2 = Pedido(679, '16/11/2022', 235, 'Agenda 2023 Cactus', 1, 'Envío Nacional=5 - Envío internacional=10')
Pedido3 = Pedido(680, '19/11/2022', 236, 'Funko Harley Queen', 1, 'Envío Nacional=5 - Envío internacional=10')

i = 0
lista = [cliente1, cliente2, cliente3]
lista_pedidos = [Pedido1, Pedido2, Pedido3]
lista_productos = []


def mostrarLista():
    k = 0
    while k < len(lista):
        print(lista[k].id_cliente, ' ', lista[k].nombre_cliente, ' ', lista[k].apellidos, ' ', lista[k].domicilio, ' ',
              lista[k].poblacion, ' ', lista[k].provincia, ' ', lista[k].cp, '', lista[k].pais, ' ', lista[k].telefono,
              '', lista[k].mail)
        k += 1


def mostrarCompra():
    k = 0
    while k < len(lista_productos):  # id_producto, nombre_producto, categoria, unitstock, precio, fecha_fabricacion
        print(lista_productos[k].id_producto, lista_productos[k].nombre_producto, lista_productos[k].categoria,
              lista_productos[k].unitstock, lista_productos[k].precio, lista_productos[k].fecha_fabricacion)
        k += 1


while i == 0:  # while
    print('Menu')
    print('1.Registrar usuario')
    print('2.Consultar Usuarios')
    print('3.Seleccionar productos')
    print('4.Comprar')
    print('5.Seguimiento pedido')
    print('6.Salir')
    opcion = int(input())
    if opcion == 1:
        print('Registrar ***')
        id = input('Introduce tu id: ')
        n = input('Introduce tu nombre: ')
        a = input('Introduce tus apellidos: ')
        d = input('Introduce tu dirección: ')
        po = input('Población: ')
        pr = input('Provincia: ')
        cp = input('Código postal: ')
        p = input('País: ')
        t = input('Teléfono contacto: ')
        m = input('Dirección de correo electrónico: ')
        cliente = Cliente(id, n, a, d, po, pr, cp, p, t, m)
        lista.append(cliente)
        print('Usuario registrado con éxito')
    elif opcion == 2:
        print('Mostrar')
        mostrarLista()
    elif opcion == 3:
        print('Seleccione producto:')
        print(f'1.{Producto1.nombre_producto}, {Producto1.precio}')
        print(f'2.{Producto2.nombre_producto}, {Producto2.precio}')
        print(f'3.{Producto3.nombre_producto}, {Producto3.precio}')
        print(f'4.{Producto4.nombre_producto}, {Producto4.precio}')
        print(f'5.{Producto5.nombre_producto}, {Producto5.precio}')
        seleccion_producto = int(input())
        if seleccion_producto == 1:
            lista_productos.append(Producto1)
            print(f'{Producto1.nombre_producto} ha sido añadido al carrito.')
        elif seleccion_producto == 2:
            lista_productos.append(Producto2)
            print(f'{Producto2.nombre_producto} ha sido añadido al carrito.')
        elif seleccion_producto == 3:
            lista_productos.append(Producto3)
            print(f'{Producto3.nombre_producto} ha sido añadido al carrito.')
        elif seleccion_producto == 4:
            lista_productos.append(Producto4)
            print(f'{Producto4.nombre_producto} ha sido añadido al carrito.')
        elif seleccion_producto == 5:
            lista_productos.append(Producto5)
            print(f'{Producto5.nombre_producto} ha sido añadido al carrito.')
        else:
            print('El producto seleccionado no es válido.')
    elif opcion == 4:
        print('Proceder a pasarela de pago.')
        print('Estos son los productos que vas a comprar:\n')
        mostrarCompra()
        compra = int(input('Si quieres continuar con la compra pulsa 1, sino pulsa 2.'))
        if compra == 1:
            Pedido.pagado()
        elif compra == 2:
            print('Vas a salir del programa')
            exit()

    elif opcion == 5:
        Pedido.enviarSMS(lista_productos)
    elif opcion == 6:
        exit()
    else:
        print('Opción no válida.')
