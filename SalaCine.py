'''
La clase SalaCine representa la sala con un mapa de silla 
una sala con muchos objetos silla
'''
import Silla as file_silla

class SalaCine:
    '''
    Constructor que genera las instancias que se van a tener en cuenta
    '''
    def __init__(self, filas=0, columnas=0):
        self.filas = filas
        self.columnas = columnas
        self.mapa_sala = []

    def crear_sala(self):
        '''
        Función que genera la sala con las filas y columnas ingresadas por el usuario
        Además, establece la numeración A1, A2...
        '''
        for cont_row in range (1,self.filas+1):
            letra_fila = chr(64+cont_row)
            for cont_col in range(1, self.columnas+1):
                pos_silla = f"{letra_fila}{cont_col}"
                self.mapa_sala.append(file_silla.Silla(pos_silla))

    def get_sala(self):
        '''
        Retorna el mapa de la sala creado
        '''
        return self.mapa_sala
    
    def mostrarMapaSillas(self):
        '''
        Esta función realiza la muestra del mapa de las sillas generadas
        por el usuario
        
        Realiza la consulta de qué sillas están reservadas, 
        si está reservada va generar una salida [A1], si no, estará 
        de manera general A1
        '''
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
