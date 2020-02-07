from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    form = '''
    <form class="auth-form" action = "/search" method="GET">
    <div> Откуда <input type="text" name="t_departure" />  </div>
    <div> Куда <input type="text" name="t_direction" /> </div>
    <div> Дата <input type="text" name="t_date" /> </div>
    <div> <input type="submit" value="Подобрать" />  </div>
    </form>
    '''

    return form

@app.route('/search', methods=["POST", "GET"])
def search():
    date = request.form.get("t_date")
    direcrtion = request.form.get("t_direction")
    depature = request.form.get("t_departure")
    return f"Летим {date} из {depature} в {direcrtion}"

if __name__ == '__main__':
    app.run()