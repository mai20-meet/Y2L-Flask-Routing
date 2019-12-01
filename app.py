from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"



@app.route('/')
def home():
	return render_template("home.html")

@app.route('/store')
def store():
	return render_template("store.html", p = query_all(), name = "bonzo")


@app.route('/cart')
def cart():
	
	return render_template("cart.html")

@app.route('/add_product')
def add_the_product():
	name = request.form['name']
	price = request.form['price']
	picture_link = request.form['picture_link'] 
	description = request.form['description']
	add_the_product(name, price, picture_link, description)
	return render_template("store.html")

@app.route('/update_product_status')
def update_the_product_status():
	name = request.form['name']
	price = request.form['price']
	picture_link = request.form['picture_link'] 
	description = request.form['description']
	update_the_product_status(name, price, picture_link, description)
	return render_template("store.html")




if __name__ == '__main__':
	app.run(debug=True)