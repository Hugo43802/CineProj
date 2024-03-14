import Silla as file_silla

class SalaCine:
    def __init__(self, filas=0, columnas=0):
        self.filas = filas
        self.columnas = columnas
        self.mapa_sala = []

    def crear_sala(self):
        pos_silla=1
        for _ in range (1,self.filas+1):
            letra_fila = chr(64+pos_silla)
            for _ in range(1, self.columnas+1):
                num_silla = f"{letra_fila}{pos_silla}"
                self.mapa_sala.append(file_silla.Silla(num_silla))
                pos_silla+=1

    def get_sala(self):
        return self.mapa_sala
    
    def mostrarMapaSillas(self):
        for list_sillas in self.mapa_sala:
            for silla in list_sillas:
                print(silla.mostrar_numsilla(), end="")
            print()

# cine = SalaCine(3,4)
# cine.crear_sala()
# cine.mostrarMapaSillas()
