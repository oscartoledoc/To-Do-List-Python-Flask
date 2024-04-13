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





MariaDB [(none)]> SHOW TABLES;
ERROR 1046 (3D000): No database selected
MariaDB [(none)]> USE contacts.db
ERROR 1049 (42000): Unknown database 'contacts.db'
MariaDB [(none)]> USE contactsdb;
Database changed
MariaDB [contactsdb]> SHOW TABLES;
Empty set (0.038 sec)

MariaDB [contactsdb]> CREATE Contact;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'Contact' at line 1
MariaDB [contactsdb]> SHOW TABLES;
Empty set (0.003 sec)

MariaDB [contactsdb]> SHOW TABLES;
+----------------------+
| Tables_in_contactsdb |
+----------------------+
| alembic_version      |
| contact              |
+----------------------+
2 rows in set (0.001 sec)

MariaDB [contactsdb]> SELECT * FROM contact
    -> Bye
Ctrl-C -- exit!

C:\xampp\mysql\bin>mysql -u root -p
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 14
Server version: 10.4.32-MariaDB mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> USE contactsdb;
Database changed
MariaDB [contactsdb]> SHOW TABLES;
+----------------------+
| Tables_in_contactsdb |
+----------------------+
| alembic_version      |
| contact              |
+----------------------+
2 rows in set (0.001 sec)

MariaDB [contactsdb]> SELECT * FROM contact;
+----+----------+---------------------------+-----------+
| id | fullname | email                     | phone     |
+----+----------+---------------------------+-----------+
|  1 | Oscar    | oscartoledo1799@gmail.com | 932494159 |
+----+----------+---------------------------+-----------+
1 row in set (0.001 sec)

MariaDB [contactsdb]> SELECT * FROM contact;
+----+----------+---------------------------+-----------+
| id | fullname | email                     | phone     |
+----+----------+---------------------------+-----------+
|  1 | Oscar    | oscartoledo1799@gmail.com | 932494159 |
|  2 | Oscar    | oscartoledo1799@gmail.com | 932494159 |
+----+----------+---------------------------+-----------+
2 rows in set (0.022 sec)