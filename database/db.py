import mysql.connector

def connectDB():
    try:
        mydb =  mysql.connector.connect(
            host="localhost",
            user="root",
            password="9811810fz",
            database="erp"
        )    
    except:
        mydb =  mysql.connector.connect(
            host="localhost",
            user="root",
            password="9811810fz"
        )

        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE erp")
        mycursor.execute("USE erp")
        mycursor.execute("CREATE TABLE clients (client_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,client_number INT, \
            client_name VARCHAR(255), client_address VARCHAR(255), \
            client_phone VARCHAR(15), client_email VARCHAR(50))")

def insertClient(client_number, client_name, client_address, client_phone, client_email):
    mydb =  mysql.connector.connect(
        host="localhost",
        user="root",
        password="9811810fz"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO clients (client_number, client_name, client_address, client_phone, client_email) \
    VALUES (%s, %s, %s)"
    val = (client_number, client_name, client_address, client_phone, client_email)
    mycursor.execute(sql, val)
    mydb.commit()
