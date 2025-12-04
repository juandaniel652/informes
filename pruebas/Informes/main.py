#Importar módulos
import predicacion_del_grupo
import base_de_datos
import archivar_excel

#PROGRAMA PRINCIPAL

#Entrada de datos
creacion_de_base_de_datos = base_de_datos.crear_base_de_datos()

grupo_5 = ["Arteaga Bedoya Eva", "Bedoya Callejas Eva", "Dominguez Juan", "Dominguez Miriam", "Dominguez Patricio",
           "Encina Gerardo", "Encina Monica", "Gonchay Brenda", "Gonchay Ema", "Morales Nahiara", 
           "Morales Ramona", "Ovejero Gsutavo", "Viera Alex", "Viera Cristian", "Viera Valeria"]

total_de_publicadores = len(grupo_5)

#Total Meses
meses = ['', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
         'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

#Total de Precursores (Auxiliares y Regulares)
precursores_del_grupo = ['Encina Gerardo', 'Encina Monica', 'Dominguez Juan']
precursores_con_horas_extra = ['Encina Gerardo', 'Encina Monica']

entrada_mes = int(input("Mes (número): "))
entrada_anio = int(input("Año: "))

for indice, integrante in enumerate (grupo_5) : 

    entrada_nombre = integrante
    entrada_actividad = input(f"{integrante} ¿Realizó actividad? [Si/No]?: ").strip().lower() == "si"
    entrada_cursos_biblicos = int(input("Cursos Bíblicos: "))

    #Funciones
    recuento_de_informes = predicacion_del_grupo.Informes(entrada_nombre, entrada_actividad, entrada_cursos_biblicos, entrada_mes, entrada_anio)
    informes_de_predicacion = recuento_de_informes.agrupar()

    #Precursores y No Precursores

    if entrada_nombre in precursores_del_grupo :

        entrada_horas = int(input("Horas: "))
        recuento_de_precursores = predicacion_del_grupo.Precursorado(entrada_nombre, entrada_actividad, entrada_cursos_biblicos, meses[entrada_mes], entrada_anio, str(entrada_horas), 0, 0)

        if entrada_nombre in precursores_con_horas_extra : 

            entrada_horas_sae = int(input("Horas SAE: "))
            entrada_horas_ldb = int(input("Horas LDB: "))
            recuento_de_precursores = predicacion_del_grupo.Precursorado(entrada_nombre, entrada_actividad, entrada_cursos_biblicos, meses[entrada_mes], entrada_anio, str(entrada_horas), str(entrada_horas_sae), str(entrada_horas_ldb))

        precursores = recuento_de_precursores.agrupar_horas()
        entrada_de_base_de_datos = base_de_datos.guardar_datos(precursores) 

    else : 

        recuento_de_publicadores = predicacion_del_grupo.Precursorado(entrada_nombre, entrada_actividad, entrada_cursos_biblicos, meses[entrada_mes], entrada_anio, '', '', '')
        publicadores = recuento_de_publicadores.agrupar_horas()
        entrada_de_base_de_datos = base_de_datos.guardar_datos(publicadores)


#Convertir a Excel

guardar_a_excel = input("¿Desea gurdar a una planilla excel?: ")

if guardar_a_excel.lower() == 'si' : 
    
    planillas = archivar_excel.convertir_a_excel_por_mes(meses[entrada_mes])