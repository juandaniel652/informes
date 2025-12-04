from usuarios.publicador import Publicador
from usuarios.precursor import Precursor
from usuarios.precursor_especial import PrecursorEspecial
from base_datos.gestor import Gestor


class Informe:

    def __init__(self, integrantes, precursores=[], precursores_especiales=[]):
        self.integrantes = integrantes
        self.precursores = precursores
        self.precursores_especiales = precursores_especiales
        self.gestor = Gestor()

    def procesar_informes(self, mes, anio):
        meses = ['', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

        for nombre in self.integrantes:
            print(f"\n--- Registro para {nombre} ---\n")

            respuesta = input("¿Realizó actividad? [Si/No]: ").strip().lower()
            if respuesta != 'si':
                print(f"{nombre} no realizó actividad. Pasando al siguiente...\n")
                continue

            actividad = True
            cursos_biblicos = int(input("Cantidad de cursos bíblicos: "))

            # --- Precursor Especial ---
            if nombre in self.precursores_especiales:
                horas = int(input("Horas: "))
                horas_sae = int(input("Horas SAE: "))
                horas_lbd = int(input("Horas LBD: "))
                persona = PrecursorEspecial(nombre, actividad, cursos_biblicos,
                                            meses[mes], anio, horas, horas_sae, horas_lbd)
                tipo_servicio = "N"

            # --- Precursor Regular ---
            elif nombre in self.precursores:
                horas = int(input("Horas: "))
                persona = Precursor(nombre, actividad, cursos_biblicos,
                                    meses[mes], anio, horas)
                tipo_servicio = "N"

            # --- Publicador (incluye Auxiliares) ---
            else:
                # Publicador regular o Precursor Auxiliar
                persona = Publicador(nombre, actividad, cursos_biblicos,
                                     meses[mes], anio)

                # Preguntar si es precursor auxiliar
                es_auxiliar = input("¿Es precursor auxiliar? [Si/No]: ").strip().lower()
                if es_auxiliar == 'si':
                    while True:
                        tipo_servicio = input("Tipo de servicio [Continuo/Solo este mes]: ").strip().capitalize()
                        if tipo_servicio in ["Continuo", "Solo este mes"]:
                            break
                        print("⚠️ Ingrese una opción válida: 'Continuo' o 'Solo este mes'.")
                else:
                    tipo_servicio = "N"

            # Guardar datos
            datos = persona.agrupar_datos()
            datos["tipo_servicio"] = tipo_servicio  # <--- añadimos el nuevo campo
            self.gestor.guardar_datos(datos)
