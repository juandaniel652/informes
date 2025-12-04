class Publicador :

    def __init__ (self, nombre, actividad, cursos_biblicos, mes, anio) :

        self.nombre = nombre
        self.actividad = actividad
        self.cursos_biblicos = cursos_biblicos
        self.mes = mes
        self.anio = anio


    def agrupar_datos (self) :
        
        return {
            "nombre": self.nombre,
            "actividad": self.actividad,
            "cursos": self.cursos_biblicos,
            "mes": self.mes,
            "anio": self.anio
        }