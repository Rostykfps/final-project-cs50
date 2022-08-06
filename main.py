from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ordersDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    mail = db.Column(db.String(50))
    car = db.Column(db.String(150))
    parts = db.Column(db.Text)

    def __repr__(self):
        return '<Orders %r>' % self.id

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/kuzov')
def kuzov():
    return render_template('kuzov.html')

@app.route('/optyka')
def optyka():
    return render_template('optyka.html')

@app.route('/radiator')
def radiator():
    return render_template('radiator.html')

@app.route('/glass')
def glass():
    return render_template('glass.html')

@app.route('/order', methods=['POST', 'GET'])
def order():
    if request.method == "POST":

        name = request.form['name']
        phone = request.form['phone']
        mail = request.form['mail']
        car = request.form['car']
        parts = request.form['parts']

        orders = Orders(name=name, phone=phone, mail=mail, car=car, parts=parts)

        try:
            db.session.add(orders)
            db.session.commit()
            return redirect('/')
        except:
            return "Не заповнені всі поля"
    else:
        return render_template('order.html')

if __name__ == "__main__":
    app.run(debug=True)

