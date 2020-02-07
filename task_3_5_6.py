from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    form = '''
    <form class="search-form" action="/search" method="GET" >
    <input type="text" name="s" />
    <input type="submit" value="Найти" />
    </form>
    '''
    return form

@app.route("/search", methods=['POST', 'GET'])
def search():
    name = request.args.get("s")
    return f"<p>Выполняем поиск по {name}</p>"

if __name__ == '__main__':
    app.run()