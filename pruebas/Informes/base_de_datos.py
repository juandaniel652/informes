import sqlite3 as sql

def crear_base_de_datos() :

    try :

        conexion = sql.connect('informes_de_predicacion_grupo_5.db')
        cursor = conexion.cursor()

        # Crear tabla si no existe
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS informes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                actividad TEXT NOT NULL,
                cursos_biblicos INTEGER NOT NULL,
                mes INTEGER NOT NULL,
                anio INTEGER NOT NULL,   
                horas TEXT NOT NULL,
                horas_sae TEXT,
                horas_LDB TEXT
            )
        ''')

        conexion.commit()
        conexion.close()

    except Exception as  error :

        print(f"Error al crear la base de datos: {error}")


def guardar_datos(informe) :

    try :

        datos = informe  # Ahora sí es una instancia

        # Convertir la lista en una tupla para la consulta SQL
        datos_tuple = tuple(dato.split(": ")[1] for dato in datos)

        conexion = sql.connect('informes_de_predicacion_grupo_5.db')
        cursor = conexion.cursor()

        # Insertar datos en la tabla (execute en vez de executemany)

        cursor.execute('''
            INSERT INTO informes (nombre, actividad, cursos_biblicos, mes, anio, horas, 
                    horas_sae, horas_LDB)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', datos_tuple)

        conexion.commit()
        conexion.close()

        print("Datos guardados correctamente.")


    except Exception as error :

        print(f"Error al guardar los datos: {error}")