import Usuario as file_usuario
'''
Clase que permite al usuario interactuar con el resto de clases
'''
class Menu:
    def __init__(self):
        self.usuario = None    
    
    def mostrar_menu(self):
        salir = False

        while not salir:
            print("\n1. Nombre admin")
            print("2. Crear sala")
            print("3. Crear reserva")
            print("4. Consultar reserva")
            print("5. Cancelar reserva")
            print("6. Salir")

            op = input("\nSeleccione una opción: ")
            if op == "1":
                nombre = input("Por favor digite su nombre: ")
                self.usuario = file_usuario.Usuario(nombre)
            elif op == "2":
                fila = int(input("Ingrese el número de filas: "))
                columna = int(input("Ingrese el número de columnas: "))
                self.usuario.crear_sala(fila,columna)
                #Mostrar el mapa de la sala apenas se crea
                self.usuario.salas[0].mostrarMapaSillas()
            elif op == "3":
                print("SE REALIZARÁ LA RESERVA")
                num_sala = 0
                sillas = input("Ingrese las posiciones de las sillas: ").split()
                self.usuario.crear_reserva(num_sala, *sillas)
            elif op == "4":
                self.usuario.consultar_reserva()
                self.usuario.salas[0].mostrarMapaSillas()
            elif op == "5":
                num_sala = 0
                reservas = input("Ingrese el (los) número(s) de la reserva: ").split()
                self.usuario.cancelar_reserva(num_sala, *reservas)
            elif op == "6":
                salir = True
def main():
    '''
    Se crea las instancia de la clase menú, mostrando 
    la ejecución del método mostrar_menu
    '''
    menu = Menu()
    menu.mostrar_menu()
'''
Esta instrucción permite generar que la ejecución del código sea
única, entendiendo que al tener diferentes clases podrá fallar si 
llama diferentes clases al mismo tiempo.
'''
if __name__ == "__main__":
    main()
