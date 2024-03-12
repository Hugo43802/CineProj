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
        return res

    def cancelar_reserva(self):
        pass

    def consultar_reserva(self):
        lista_sillas = []
        for clave in self.reservas:
            lista_sillas.append(self.reservas[clave]) 
        print(f"{self.nombre} ha reservado las sillas: {lista_sillas}")

    def borrar_sala(self):
        pass

    def mostrar_salas(self):
        pass

user = Usuario("Hugo")
user.crear_sala(6,6)
reserv = user.crear_reserva(0,1,2,3)
print(reserv)
user.consultar_reserva()




