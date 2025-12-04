from usuarios.publicador import Publicador

class Precursor (Publicador) :

    def __init__ (self, nombre, actividad, cursos_biblicos, mes, anio, horas) :

        super().__init__(nombre, actividad, cursos_biblicos, mes, anio)
        self.horas = horas

    def agrupar_datos (self) :
        
        datos = super().agrupar_datos()
        datos["horas"] = self.horas
        return datos