from flask import Flask, request

app = Flask(__name__)


@app.route('/request')
def index():
    form = '''
    <h2>Платежные данные</h2>
    <form class="card-form" action = "/pay" method="post">
    <div> <input type="text" name="card_number" /></div>
    <div> 
    <input type="text" name="card_name" />   
    <input type="text" name="card_expires" />  
    </div>
    <div> <input type="text" name="card_cvv2" /></div>
    <div> <input type="submit" value="Оплатить" /></div>
    </form>
    '''
    return form


@app.route("/pay", methods=['POST', 'GET'])
def pay():
    card_number = request.form.get("card_number")
    card_name = request.form.get("card_name")
    card_expires = request.form.get("card_expires")
    card_cvv2 = request.form.get("card_cvv2")
    return f"Карта: {card_number}\nВладелец: {card_name}\nДействует до: {card_expires}\nКод безопасности: {card_cvv2}"


if __name__ == '__main__':
    app.run()