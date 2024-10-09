import sqlite3
from Automovil import Automovil

con = sqlite3.connect('base_autos.db')

cursor = con.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS automoviles 
                (id_automovil INTEGER PRIMARY KEY, 
                marca TEXT,
                color TEXT,
                modelo TEXT,
                velocidad INTEGER,
                ruedas INTEGER,
                año INTEGER)  ''')

automovil_dos = Automovil("Verde","toyota",13,140,4,"asd",2000)

datos = [automovil_dos.marca,automovil_dos.color,automovil_dos.get_modelo(),automovil_dos.velocidad,automovil_dos.ruedas,automovil_dos.get_año()]

cursor.execute(''' INSERT INTO automoviles(marca,color,modelo,velocidad,ruedas,año) 
               values (?,?,?,?,?,?)''',datos)

con.commit() # Commit() se utiliza para guardar los datos en la base de datos.

cursor.execute('SELECT * FROM automoviles')

filas = cursor.fetchall() # Permite recuperar todos los datos de una consulta ejecutada

for fila in filas:
    print(fila)

cursor.close() #Cierra el cursor
con.close() # Cierra la conexion con la base de datos.