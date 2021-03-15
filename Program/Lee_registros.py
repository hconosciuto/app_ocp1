from flask import Flask, render_template
import os, time
import psycopg2

app = Flask(__name__)
@app.route("/")
def muestra():

    registros = leo_registros()
    return render_template("test.html", data=registros)

        
def leo_registros():
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

    # Si la tabla no existe me quedo espeando un delay de 10'' hasta que se cree.
    # Esto es por si se instancia primero el pod que crea los registros y la tabla.
    while existe_tabla < 1:

        print ("Esperando que se cree la tabla" + ptabla + "...")
        time.sleep(10)
        cur.execute(CONSULTA)
        existe_tabla = cur.fetchone()[0]

    # Si la tabla existe leo los registros y los almaceno en una lista.
    CONSULTA= "SELECT TO_CHAR(fecha::timestamp, 'DD-Mon-YYYY HH24:MM:SS'), nombre FROM " + ptabla + " order by fecha;"

    cur.execute(CONSULTA)

    rows = cur.fetchall()        

    # Inicializo la lista con los registros para no duplicarlos.
    registros = []

    # Recorro el set de registos.
    for reg in rows:

        registro = reg[0] , reg[1]

        registros.append(registro)

    return tuple(registros)


# Defino Variables generales.
registros = []

# Leo las variables para conectarme a Postgresql.
phost = os.environ['hac_PHOST']
puser = os.environ['hac_PUSERNAME']
pdatabase = os.environ['hac_PDATABASE']
ppassword =  os.environ['hac_PPASSWORD']
ptabla =  os.environ['hac_PTABLA']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # pragma: no cover
    
# Cierro la conexión a la base.
#cur.close()

