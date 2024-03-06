class Silla:

    def __init__(self, num_Silla):
        self.numSilla = num_Silla
        self.reserva = False
    
    def reservar(self):
        self.reserva = True

    def cancelar_reserva(self):
        self.reserva = False
    
    def consultar_reserva(self):
        return self.reserva
    
    def mostrar_numsilla(self):
        return self.numSilla


# sillas=[Silla(i) for i in range(6)]
# for num,chair in enumerate(sillas):
#     if num % 2 == 0:
#         chair.reservar()
#     chair.consultar_reserva()

