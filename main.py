from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
import mail
import app as client_app
import helper

helper.helper

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'

db = SQLAlchemy(app)

class users(db.Model):
	id = db.Column("id",db.Integer,primary_key=True)
	name = db.Column("name",db.String(100))
	email = db.Column("email",db.String(100))

	def __init__(self,name,email):
		self.name = name
		self.email = email


@app.route("/")
def home():
	return render_template('index.html')

@app.route("/<other>")
def other(other):
	return render_template('other.html',name= other)

@app.route("/success",methods=["POST","GET"])
def completed():
	if request.method == "GET":
		return render_template('index.html')
	else:
		name = request.form["name"]
		email = request.form["pass"]
		usr = users(name,email)
		db.session.add(usr)
		mail.first_mail(client_app.return_table(), email,name)
		db.session.commit()  
		#name_email()
		return render_template('success.html',name= name)

def name_email():
	name = []
	email = [] 
	all_users = users.query.all()
	for item in all_users:
		name.append(item.name)
		email.append(item.email)

	#print(email)
	return name,email


if __name__ == '__main__':
	db.create_all()
	app.run(debug = True)