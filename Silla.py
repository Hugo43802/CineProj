'''
La clase silla representa el objeto silla en una sala de cine
para los set se utilizará la reserva ya sea como true o false
y los get devuelven el estado de la silla
'''
class Silla:

    def __init__(self, pos_Silla):
        self.pos_Silla = pos_Silla
        self.reserva = False
    
    def reservar(self):
        self.reserva = True

    def cancelar_reserva(self):
        self.reserva = False
    
    def consultar_reserva(self):
        return self.reserva
    
    def mostrar_pos_silla(self):
        return self.pos_Silla


# sillas=[Silla(i) for i in range(6)]
# for num,chair in enumerate(sillas):
#     if num % 2 == 0:
#         chair.reservar()
#     chair.consultar_reserva()

