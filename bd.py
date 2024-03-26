import mysql.connector

conexao = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    database = "usuarios"
)

cursor = conexao.cursor()

userEmail = "anatxzier@gmail.com"
userPass = "123"
comando = f'INSERT INTO Usuario (userEmail, userPass) VALUES ("{userEmail}", "{userPass}")'
cursor.execute(comando)
conexao.commit()

comando2 = 'SELECT * from Usuario'
cursor.execute(comando2)
resultados = cursor.fetchall()
print(resultados)

cursor.close()
conexao.close()