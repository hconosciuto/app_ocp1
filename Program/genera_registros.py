# ******************************************************************************************************************
# * genera_registros.py: Aplicación para usar en las Demos de OCP Infra.
# * Parte del repositorio: https://github.com/hconosciuto/app_ocp1
# * Creada por: Hernan Conosciuto - Marzo 2021.
# * Descripción: Genera nombres random con timestamp en un postgresql.
# * Historial:
# * 20201-03-16: Hernan - Cambio a public el repo y agregado de variable para tiempo del sleep.
# ******************************************************************************************************************

import psycopg2, os, random, time
from datetime import datetime


# Leo las variables para conectarme a Postgresql.
phost = os.environ['hac_PHOST']
puser = os.environ['hac_PUSERNAME']
pdatabase = os.environ['hac_PDATABASE']
ppassword =  os.environ['hac_PPASSWORD']
ptabla =  os.environ['hac_PTABLA']
tiempo = int(os.environ['hac_TIEMPO'])

# Armo las ilstas de nombres y apellidos

Nombres=('Hernan', 'Ignacio', 'Guadalupe', 'Claudia', 'Ana', 'Carina','Paulo', 'Alejandro', 'Martin', 'Christian', 'Bruno',\
         'Federico','Magda', 'Tomas','Fernando','David','Mariela','Lucia')
Apellidos=('Garcia', 'Gomez', 'Lopez', 'Rodriguez', 'Fenandez', 'Gonzalez','Pereyra','Acosta','Medina','Gimenez', 'Molina')

# Funcion que crea nombres completos Random
def crea_nombres():

    nombre_completo = random.choice(Nombres) + " " + random.choice(Apellidos)

    return(nombre_completo)
    

# Genero la conexion con la base. 
try:
    
    conn = psycopg2.connect(
        host = phost,
        database = pdatabase,
        user = puser,
        password = ppassword
    )
    print('Database connected!.')

except:
    print('Database not connected.')

# Creo el cursor.
cur = conn.cursor()

# Valido si existe la tabla que voy a utilizar.
CONSULTA = "SELECT count(1) FROM information_schema.tables WHERE table_name = '" + ptabla + "';"

cur.execute(CONSULTA)

existe_tabla = cur.fetchone()[0]

# Si la tabla no existe...
if existe_tabla < 1:

    # Creo la tabla.
    CONSULTA = "CREATE TABLE " + ptabla + "  (fecha TIMESTAMP without time zone NULL, nombre varchar(30));"
    print(CONSULTA)
    print (cur.execute(CONSULTA))
    conn.commit()

    print("Tabla " + ptabla + " creada!")

# Loop principal.
while True:

    # Obtengo la fecha y hora
    # current date and time
    ahora = datetime.now()
    vfecha = ahora.strftime("%Y-%m-%d %H:%M:%S")

    nombre = crea_nombres()
    print (nombre)
    CONSULTA = "INSERT INTO " + ptabla + " (fecha, nombre) values ('" + vfecha +\
              "', '" + nombre + "'); "

    cur.execute(CONSULTA)
    
    conn.commit()  

    # Espero 5 segundos
    time.sleep(tiempo)


# Cierro la conexión a la base.
cur.close()

