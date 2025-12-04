class Informes :

    def __init__ (self, nombre, actividad, cursos_biblicos, mes, anio) :

        self.nombre = nombre
        self.actividad = actividad
        self.cursos_biblicos = cursos_biblicos
        self.mes = mes
        self.anio = anio

    def agrupar(self) :

        return [
            f'Nombre: {self.nombre}',
            f'Actividad: {"Sí" if self.actividad else "No"}',
            f'Cursos Bíblicos: {self.cursos_biblicos}',
            f'Mes: {self.mes}',
            f'Año: {self.anio}'
        ]


class Precursorado(Informes) :

    def __init__(self, nombre, actividad, cursos_biblicos, mes, anio, horas, horas_sae, horas_ldb) :

        super().__init__(nombre, actividad, cursos_biblicos, mes, anio)

        self.horas = horas
        self.horas_sae = horas_sae
        self.horas_ldb = horas_ldb

    def anadir_horas_especiales (self) :

        return [
            f'Horas SAE: {self.horas_sae}',
            f'Horas LDB: {self.horas_ldb}',
        ]

    def agrupar_horas (self) :

        informes = self.agrupar()
        informes.append(f'Horas: {self.horas}')
        informes.append(f'Horas SAE: {self.horas_sae}')
        informes.append(f'Horas LDB: {self.horas_ldb}')
        return informes