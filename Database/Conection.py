import mysql.connector

conection = mysql.connector.connect(
    host="localhost",  # Servidor
    user="root",       # Usuario de MySQL
    password="SpayCliforTom45",  # Reemplázalo con tu contraseña
    database="agenda_digital",
      port="3306"  # Reemplázalo con tu base de datos
)

if conection.is_connected():
    print("Conexión exitosa a MySQL")

cursor = conection.cursor()

cursor.execute("INSERT INTO Users (Nombre, Email, Contraseña) VALUES  ('Cele', 'cele@example.com', 'k8sw34rt')")
conection.commit()

# Leer datos
cursor.execute("SELECT * FROM Users")
for usuario in cursor.fetchall():
    print(usuario)

# Cerrar conexión
cursor.close()
# Cerrar conexión
conection.close()
