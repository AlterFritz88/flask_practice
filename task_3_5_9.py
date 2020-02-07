from flask import Flask, request

app = Flask(__name__)

@app.route('/login')
def index():
    form ='''
    <h2>Авторизация</h2> 
    <form class="auth-form" action="/pay" method="POST">
    <div> Логин <input type="text" name="u_name" />  </div>
    <div> Пароль <input type="password" name="u_pass" /> </div>
    <div> <input type="submit" value="Отправить" />  </div>
    </form>
    '''

    return form

@app.route("/pay", methods=["POST", "GET"])
def pay():
    login = request.form.get("u_name")
    password = request.form.get("u_pass")
    if login == "user@stepik.org" and password == "12345":
        return "OK"
    else:
        return "ERROR"

if __name__ == '__main__':
    app.run()