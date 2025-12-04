from usuarios.publicador import Publicador
from usuarios.precursor import Precursor

class PrecursorEspecial (Precursor) :

    def __init__ (self, nombre, actividad, cursos_biblicos, mes, anio, horas, horas_sae, horas_lbd) :

        super().__init__ (nombre, actividad, cursos_biblicos, mes, anio, horas)
        self.horas_sae = horas_sae
        self.horas_lbd = horas_lbd


    def agrupar_datos (self) :
        
        datos = super().agrupar_datos()
        datos["horas_sae"] = self.horas_sae
        datos["horas_lbd"] = self.horas_lbd
        return datos
