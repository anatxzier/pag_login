from flask import Flask, render_template, redirect, url_for, request
import mysql.connector

app = Flask(__name__)


@app.route("/")
def pag_inicial():
    return render_template("Index.html")


@app.route("/bemvindo")
def bemvindo():
    return render_template("pag.html")

@app.route("/Login", methods=['GET', 'POST'])
def verificacao():
    conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    database="usuarios"
)
    if request.method == 'POST':
        userEmail = request.form['email']
        userPass = request.form['password']
        cursor = conexao.cursor()

        comando = 'SELECT * FROM usuario WHERE userEmail = %s and userPass = %s'
        cursor.execute(comando, (userEmail, userPass,))
        resultados = cursor.fetchall()

        if resultados:
            cursor.close()
            conexao.close()
            return redirect(url_for('bemvindo'))
        
        else:
            cursor.close()
            conexao.close()
            return redirect(url_for('pag_inicial'))
        
    else:

        return redirect(url_for('pag_inicial'))




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
