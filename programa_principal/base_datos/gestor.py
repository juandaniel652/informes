import sqlite3 as sql

class Gestor:

    def __init__(self, nombre_db='informes_grupo_5.db'):
        self.nombre_de_la_base_de_datos = nombre_db

    def crear_base_de_datos(self):
        try:
            conexion = sql.connect(self.nombre_de_la_base_de_datos)
            cursor = conexion.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS informes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    actividad TEXT NOT NULL,
                    cursos_biblicos INTEGER NOT NULL,
                    mes TEXT NOT NULL,
                    anio INTEGER NOT NULL,   
                    horas TEXT NOT NULL,
                    horas_sae TEXT,
                    horas_lbd TEXT
                )
            ''')
            conexion.commit()

            # --- Verifica si la columna tipo_servicio existe ---
            cursor.execute("PRAGMA table_info(informes)")
            columnas = [col[1] for col in cursor.fetchall()]
            if "tipo_servicio" not in columnas:
                cursor.execute("ALTER TABLE informes ADD COLUMN tipo_servicio TEXT DEFAULT 'Continuo'")
                conexion.commit()
                print("Columna 'tipo_servicio' agregada correctamente.")

            conexion.close()
            print("Base de datos verificada correctamente.")

        except Exception as error:
            print(f"Error al crear/verificar la base de datos: {error}")

    def guardar_datos(self, informe):
        try:
            datos = informe  # diccionario con datos del informe

            datos_tuple = (
                datos["nombre"],
                "Sí" if datos["actividad"] else "No",
                datos["cursos"],
                datos["mes"],
                datos["anio"],
                datos.get("horas", ""),
                datos.get("horas_sae", ""),
                datos.get("horas_lbd", ""),
                datos.get("tipo_servicio", "N")  # por defecto
            )

            conexion = sql.connect(self.nombre_de_la_base_de_datos)
            cursor = conexion.cursor()

            cursor.execute('''
                INSERT INTO informes (nombre, actividad, cursos_biblicos, mes, anio, horas, 
                        horas_sae, horas_lbd, tipo_servicio)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', datos_tuple)

            conexion.commit()
            conexion.close()

            print("Datos guardados correctamente.")

        except Exception as error:
            print(f"Error al guardar los datos: {error}")
