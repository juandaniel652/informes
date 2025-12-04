import pandas as pd
import sqlite3 as sql

def convertir_a_excel_por_mes (mes, anio) :

    try:
        conexion = sql.connect("informes_grupo_5.db")

        # Seleccionar solo las columnas necesarias, excluyendo 'id'
        consulta = f"""
            SELECT nombre, actividad, cursos_biblicos, mes, anio, horas, horas_sae, horas_LBD
            FROM informes
            WHERE mes = '{mes}'
            ORDER BY nombre ASC
        """

        datos = pd.read_sql_query(consulta, conexion)

        # Exportar a Excel
        datos.to_excel(f"Informe_del_mes_de_{mes}_{anio}.xlsx", index=False, engine="openpyxl")
        conexion.close()

        print('Los datos se han guardado exitósamente en el Excel.')

    except Exception as error :
        
        print(f"Error al exportar a Excel: {error}")

convertor = convertir_a_excel_por_mes("Octubre", 2025)
