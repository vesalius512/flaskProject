from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Wish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120))
    granted = db.Column(db.Boolean)


@app.route('/delete/<int:wish_id>')
def delete(wish_id):
    wish = Wish.query.filter_by(id=wish_id)[0]
    db.session.delete(wish)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/update/<int:wish_id>')
def edit(wish_id):
    wish = Wish.query.filter_by(id=wish_id)[0]
    wish.granted = not wish.granted
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/', methods=['GET', 'POST'])
def index():
    wish_list = Wish.query.all()
    return render_template('index.html', wish_list=wish_list)


@app.route('/make', methods=['POST'])
def make():
    text = request.form.get('item')
    wish = Wish(text=text, granted=False)
    db.session.add(wish)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
