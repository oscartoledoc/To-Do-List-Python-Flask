# ToDoList_Flask
This is a CRUD application. This is a notes app, you can create, read, modify and delete your notes.

Es recomendable que cada proyecto tenga su entorno virtual para que algunos no estén usando el mismo paquete.

Estoy usando black como formateador de código.

flask aparte de devolver tipos de valores, también puede devolver HTML.

lorem300 - es para escribir un texto de muestra

usaré XAMPP para la base de datos
instalaré SQLAlquemy tmb

usaré pip install mysqlclient para la BBDD también (me va a permitir conectarme a SQL)

venv\scripts\activate
set FLASK_DEBUG=1

Para moverme a mi root y ver la tabla que cree:
cd C:\xampp\mysql\bin
mysql -u root -p

NOTA: .gitignore para evitar que rastreé el caché.  

Puedes redirigir la salida a un archivo de texto si deseas guardar la lista de bibliotecas instaladas en un archivo:
pip freeze > requirements.txt

Esto para que se pueda instalar todo en el entorno virtual:
pip install -r requirements.txt

Cuando ves la dirección 127.0.0.1:5000 en el resultado de la ejecución de tu aplicación Flask, significa que la aplicación está en funcionamiento y lista para recibir solicitudes en tu propia máquina, en el puerto 5000. Puedes acceder a tu aplicación abriendo un navegador web y visitando http://127.0.0.1:5000 o simplemente http://localhost:5000.

CTRL + } para comentar en html

############################
COMO LE METO JAVASCRIPT PARA VENTANAS EMERGENTES AL REALIZAR OPERACIONES CRUD
############################

BOOTSTRAP DIVIDE LA PANTALLA EN 12 DIVISIONES.


## Instructions to enter to the database
MariaDB [(none)]> USE contactsdb;
Database changed
MariaDB [contactsdb]> SHOW TABLES;
Empty set (0.038 sec)

MariaDB [contactsdb]> CREATE Contact;
MariaDB [contactsdb]> SHOW TABLES;
+----------------------+
| Tables_in_contactsdb |
+----------------------+
| alembic_version      |
| contact              |
+----------------------+
2 rows in set (0.001 sec)


MariaDB [(none)]> USE contactsdb;
Database changed
MariaDB [contactsdb]> SHOW TABLES;
+----------------------+
| Tables_in_contactsdb |
+----------------------+
| alembic_version      |
| contact              |
+----------------------+

MariaDB [contactsdb]> SELECT * FROM contact;
+----+----------+---------------------------+-----------+
| id | fullname | email                     | phone     |
+----+----------+---------------------------+-----------+
|  1 | Oscar    | oscartoledo1799@gmail.com | 932494159 |
|  2 | Oscar    | oscartoledo1799@gmail.com | 932494159 |
+----+----------+---------------------------+-----------+
