'''
La clase SalaCine representa la sala con un mapa de silla 
una sala con muchos objetos silla
'''
import Silla as file_silla

class SalaCine:
    def __init__(self, filas=0, columnas=0):
        self.filas = filas
        self.columnas = columnas
        self.mapa_sala = []

    def crear_sala(self):
        for cont_row in range (1,self.filas+1):
            letra_fila = chr(64+cont_row)
            for cont_col in range(1, self.columnas+1):
                pos_silla = f"{letra_fila}{cont_col}"
                self.mapa_sala.append(file_silla.Silla(pos_silla))

    def get_sala(self):
        return self.mapa_sala
    
    def mostrarMapaSillas(self):
        print("\nMapa de la Sala:")
        for silla in self.mapa_sala:
            if silla.consultar_reserva():
                print(f"[{silla.mostrar_pos_silla()}]", end=" ")  # Silla reservada
            else:
                print(f"{silla.mostrar_pos_silla()}", end=" ")  # Silla libre
        print()  # Nueva línea para la siguiente fila


# cine = SalaCine(3,4)
# cine.crear_sala()
# cine.mostrarMapaSillas()
