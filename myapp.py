from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask import flash,redirect,request
from forms import SubscribeForms

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://tmkokhix:XeOC1XyEkrlVJCFho0jPJTp0bl1eChL-@raja.db.elephantsql.com:5432/tmkokhix'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://postgres:nanaqhouamy@localhost/postgres'
# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///findoc.db'
app.config['SECRET_KEY'] = '2b31cddd60782ba873e49c9eb34402f6'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    firstname = db.Column(db.String(80), nullable =False)
    lastname = db.Column(db.String(80), nullable=False)
    telephone = db.Column(db.Numeric(15), nullable=False)
    email = db.Column(db.String(120), unique = True)

def __repr__(self):
        return f"User('{self.firstname}', '{self.lastname}', '{self.telephone}', '{self.email}')"

@app.route('/')
def index():
    return render_template('FinDoc.html')

@app.route('/subscribe',methods=['GET','POST'])
def sub():
     form = SubscribeForms()
     if request.method == 'POST' and form.validate_on_submit():
        sub = User(firstname= form.firstname.data, lastname= form.lastname.data, telephone= form.telephone.data, email= form.email.data,)
        db.session.add(sub)
        db.session.commit()
        flash(f'Subcribed successfully for {form.firstname.data}!','success')
        return redirect(url_for('index'))
     return render_template('form.html',form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')