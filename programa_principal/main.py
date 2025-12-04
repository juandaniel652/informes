from informes.informe import Informe 
from archivos_excel.convertir import convertir_a_excel_por_mes
from base_datos.gestor import Gestor

def main () :

    # Crear base de datos
    gestor = Gestor()
    gestor.crear_base_de_datos()


    # Grupo de personas
    integrantes_del_grupo_5 = [
        "Arteaga Bedoya Eva", "Bedoya Callejas Eva", "Bedoya Érica" , "Dominguez Juan", "Dominguez Miriam", "Dominguez Patricio",
        "Encina Gerardo", "Encina Monica", "Gonchay Brenda", "Gonchay Ema", "Morales Nahiara", 
        "Morales Ramona", "Ovejero Gustavo", "Salas Cynthia", "Salas Esteban", "Viera Alex", "Viera Cristian", "Viera Valeria"]


    #Precursores
    precursores = ['Encina Gerardo', 'Encina Monica', 'Dominguez Juan', 'Salas Esteban', 'Salas Cynthia', 
                    'Viera Valeria', 'Viera Cristian', 'Morales Ramona']
    
    precursores_especiales = ['Encina Gerardo', 'Encina Monica']


    #Entrada de horarios
    entrada_mes = int(input("Mes (número): "))
    entrada_anio = int(input("Año: "))

    # Procesar informes
    informes = Informe(integrantes_del_grupo_5, precursores, precursores_especiales)
    informes.procesar_informes(entrada_mes, entrada_anio)


    # Exportar a Excel si el usuario lo desea
    guardar_a_excel = input("¿Desea guardar a una planilla Excel?: ").strip().lower()

    if guardar_a_excel == 'si' :

        meses = ['', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        
        convertir_a_excel_por_mes(meses[entrada_mes], meses[entrada_anio])


if __name__ == "__main__":
    main()

