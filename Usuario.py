'''
Representa el sistema de reservas
'''
import SalaCine as file_cine
import Silla as file_silla

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = {}
        self.salas = []
        self.num_reservas = 0
    
    def crear_sala(self, filas, columnas):
        sala = file_cine.SalaCine(filas,columnas)
        sala.crear_sala()
        self.salas.append(sala)
    
    def crear_reserva(self, num_sala, *posiciones):
        res = []
        for posicion in posiciones:
            #Se obtiene el mapa de las salas
            mapa_sala = self.salas[num_sala].get_sala()
            #Se obtiene la posición de las sillas en sala
            pos_sillas = [x.mostrar_pos_silla() for x in mapa_sala]
            # Obtenemos el índice de pos_sillas y ese índice lo consultamos en mapa_sala
            if posicion in pos_sillas:
                indice = pos_sillas.index(posicion)
                if mapa_sala[indice].consultar_reserva() != True:
                    mapa_sala[indice].reservar()
                    res.append(self.num_reservas)
                    self.reservas[self.num_reservas] = mapa_sala[indice].mostrar_pos_silla()
                    self.num_reservas+=1
                else:
                    print(f"La silla {posicion} ya está reservada")
            else:
                print(f"La silla {posicion} no existe en la sala")
        print(f"¡{self.nombre} ha completado la reserva! Sus números de reserva son: ", res)
        return res

    def cancelar_reserva(self,sala, *num_reservas):
        for num_reserva in num_reservas:
            num_reserva = int(num_reserva)
            if num_reserva in list(self.reservas.keys()):
                #traigo la posicion que se va a eliminar de la silla
                posicion = self.reservas[num_reserva]
                mapa_sala = self.salas[sala].get_sala()
                #Se obtiene la posición de las sillas en sala
                pos_sillas = [x.mostrar_pos_silla() for x in mapa_sala]
                indice = pos_sillas.index(posicion)
                mapa_sala[indice].cancelar_reserva()
                #borrado dentro del diccionario
                del self.reservas[num_reserva]
                print(f"La reserva {num_reserva} ha sido cancelada")
            else:
                print(f"No se encontró ninguna reserva con el número {num_reserva}")
        print(f"Reservas restantes: {self.reservas}")

    def consultar_reserva(self):
        print(f"Usuario: {self.nombre}")
        for clave, valor in self.reservas.items():
            print(f"Número de reserva: {clave}, con la silla: {valor}")

def main():
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
            user = Usuario(nombre)
        elif op == "2":
            fila = int(input("Ingrese el número de filas: "))
            columna = int(input("Ingrese el número de columnas: "))
            user.crear_sala(fila,columna)
            #Mostrar el mapa de la sala apenas se crea
            user.salas[0].mostrarMapaSillas()
        elif op == "3":
            print("RESERVA")
            num_sala = 0
            sillas = input("Ingrese las posiciones de las sillas: ").split()
            user.crear_reserva(num_sala, *sillas)
        elif op == "4":
            user.consultar_reserva()
            user.salas[0].mostrarMapaSillas()
        elif op == "5":
            num_sala = 0
            reservas = input("Ingrese el (los) número(s) de la reserva: ").split()
            user.cancelar_reserva(num_sala, *reservas)
        elif op == "6":
            salir = True

if __name__ == "__main__":
    main()


