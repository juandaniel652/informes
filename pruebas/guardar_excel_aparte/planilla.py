import pandas as pd
import sqlite3 as sql

def convertir_a_excel_por_mes (mes) :

    try :  

        conexion = sql.connect("informes_de_predicacion_grupo_5.db")

        seleccionar_todo = f"SELECT * FROM informes WHERE mes == '{mes}'"
        guardado_de_datos = pd.read_sql_query(seleccionar_todo, conexion)
        guardado_de_datos.to_excel(f"Informe_del_mes_de_{mes}.xlsx", index = True, engine = "openpyxl")
        conexion.close()

        print('Los datos se han guardado exitósamente.')

    except Exception as error : 

        print(error)

entrada_mes = input("Ingrese el nombre del mes: ")
convertir = convertir_a_excel_por_mes(entrada_mes)