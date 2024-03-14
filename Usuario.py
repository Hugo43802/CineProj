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
            mapa_sala = self.salas[num_sala].get_sala()
            if posicion <= len(mapa_sala):
                silla = mapa_sala[posicion-1]
                if silla.consultar_reserva() != True:
                    silla.reservar()
                    res.append(self.num_reservas)
                    self.reservas[self.num_reservas] = silla.mostrar_numsilla()
                    self.num_reservas += 1
                else:
                    print(f"La silla {posicion} ya está reservada")
        print(f"¡{self.nombre} ha completado la reserva!")
        return res

    def cancelar_reserva(self, *num_reservas):
        for num_reserva in num_reservas:
            if num_reserva in self.reservas:
                del self.reservas[num_reserva]
                print(f"La reserva {num_reserva} ha sido cancelada")
                mapa_sala = self.salas[0].get_sala()
                for silla in mapa_sala:
                    silla.cancelar_reserva()       
            else:
                print(f"No se encontró ninguna reserva con el número {num_reserva}")
        print(f"Reservas restantes: {self.reservas}")

    def consultar_reserva(self):
        lista_sillas = []
        for clave in self.reservas.values():
            lista_sillas.append(clave)
        print(f"{self.nombre} ha reservado las sillas: {lista_sillas}")

    def borrar_sala(self):
        pass

    def mostrar_salas(self):
        pass

# user = Usuario("Hugo")
# user.crear_sala(2,2)
# reserv = user.crear_reserva(0,1,2)
# print(reserv)
# user.consultar_reserva()
# user.cancelar_reserva(0)
# user.consultar_reserva()

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
            columna = int(input("Ingrse el número de columnas: "))
            user.crear_sala(fila,columna)
        elif op == "3":
            num_sala = 0
            sillas = int(input("Ingrese las posiciones de las sillas: "))
            reserva = user.crear_reserva(num_sala, *sillas)
        elif op == "4":
            user.consultar_reserva()

if __name__ == "__main__":
    main()


