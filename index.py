import sqlite3

conexion = sqlite3.connect('Estudiante.db')

# Creamos el cursor
cursor = conexion.cursor()

# Ahora crearemos una tabla de usuarios para almacenar nombres, edades y emails
#cursor.execute('''CREATE TABLE usuarios (
#id VARCHAR(9) PRIMARY KEY,
#nombre VARCHAR(100), 
#edad INTEGER, 
#email VARCHAR(100)
#)
#''')
cursor.execute("INSERT INTO usuarios VALUES ('Yoli',26,'y@ejemplo.com')")
#cursor.execute("SELECT * FROM usuarios")
#print(cursor)

#usuario = cursor.fetchone()
#print(usuario)
 #Guardamos los cambios haciendo un commit,


 #usuarios = [
     #('1','Yoli',26,'y@ejemplo.com'),
     #('2','sebas',20,'sebas@ejemplo.com'),
     #('3','cristian',21,'y@ejemplo.com'),
     #('4','james',26,'y@ejemplo.com'),
 #]

cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)
conexion.commit()

conexion.close()