from flask import Flask, request

form = '''
    <form class="auth-form" action="/signin" method="POST">
    <div> Имя <input type="text" name="u_name" />  </div>
    <div> Фамилия <input type="text" name="u_surname" /> </div>
    <div> Почта <input type="email" name="u_mail" /> </div>
    <div> Пароль <input type="password" name="u_pass" /> </div>
    <div> Еще раз <input type="password" name="u_pass_again" /> </div>
    <div> <input type="submit" value="Зарегистрироваться" />  </div>
    </form>
'''

app = Flask(__name__)


@app.route('/signin', methods=["POST", "GET"])
def registration():
    name = request.form.get("u_name")
    surname = request.form.get("u_surname")
    mail = request.form.get("u_mail")
    pass_1 = request.form.get("u_pass")
    pass_2 = request.form.get("u_pass_again")
    try:
        if pass_1 == pass_2 and name != "" and surname != "" and mail != "" and "@" in mail:
            return f"Пользователь {name} {surname} с почтой {mail} зарегистрирован"
        else:
            return form
    except TypeError:
        return form


if __name__ == '__main__':
    app.run()