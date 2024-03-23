from flask import Flask, render_template, g
import sqlite3 
import Base

app = Flask(__name__)
#настройки приложения
app.config['DATABASE'] = 'static/bd/products.db'
app.secret_key = 'asdf1234'

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row   #как будут отражаться данные.список словарей, а не кортежей будет
    return con

def get_connect():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db    

navMenu = [
    {"link": "/index", "name": "Главная"},
    {"link": "/products", "name": "Продукция"},
    {"link": "/info", "name": "О нас"}
]

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html", menu=navMenu)

@app.route("/products")
def products():
    con = get_connect()
    base = Base.ProductDB(con)
    #base = Base.ProductDB(get_connect())
    return render_template("products.html", menu=navMenu, cards=base.getAllProduct())

@app.route("/info")
def info():
    return render_template("info.html", menu=navMenu)

@app.route("/product/<int:value>")
def prod(value):
    con = get_connect()
    base = Base.ProductDB(con)
    product = base.getProduct(value)
    #getProduct написать в классе ProductDB
    #создать шаблон и вызвать его тут
    return render_template("product.html", menu=navMenu, img=product['img'], description=product['description'], name=product['name'], price=product['price'])
#    return product['description']

#разрыв подключения
@app.teardown_appcontext
def close_connect(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__ == "__main__":
    app.run()