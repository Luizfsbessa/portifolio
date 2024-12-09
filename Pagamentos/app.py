from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Teste simples de login sem conexão com banco de dados
        if username == "admin" and password == "senha":
            session["logged_in"] = True
            return redirect(url_for("dashboard"))
        else:
            return "Usuário ou senha inválidos!", 401

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return "Bem-vindo ao Sistema de Gestão de Pagamentos"

if __name__ == "__main__":
    app.run(debug=True)
