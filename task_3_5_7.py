from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    form = '''
    <h2>Заказать консультацию</h2>
    <form class="request-form" method="POST" action = "/send" >
    <div> <input type="text" name="r_name" /> Имя </div>
    <div> <input type="text" name="r_phone" /> Телефон </div>
    <div> <input type="text" name="r_mail" /> Почта </div>
    <div> <input type="submit" value="Отправить" />  </div>
    </form>
    '''
    return form


@app.route("/send", methods=['POST', 'GET'])
def send():
    name = request.form.get("r_name")
    phone = request.form.get("r_phone")
    mail = request.form.get("r_mail")
    return f"Новая заявка от {name}, телефон: {phone}, почта: {mail}"


if __name__ == '__main__':
    app.run()