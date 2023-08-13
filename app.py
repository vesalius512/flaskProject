from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL

app = Flask(__name__)


mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'c0deandw33d'
app.config['MYSQL_DATABASE_DB'] = 'WishList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


wish_list = []


def list_append(item):
    global wish_list
    wish_list.append(item)


def list_delete(item):
    global wish_list
    wish_list.remove(item)


def list_edit(item):
    global wish_list
    wish_list.remove(item)


@app.route('/', methods=['GET', 'POST'])
def index():
    global wish_list
    if request.method == 'POST':
        item_added = request.form['item']
        if item_added != '':
            list_append(item_added)
    return render_template('index.html', wish_list=wish_list)


@app.route('/delete/<item>')
def delete(item):
    list_delete(item)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug = True)