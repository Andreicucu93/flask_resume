from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

#Create index page
def index():
	first_name = "Andrei"
	favorite_pizza = ['Pepperoni', 'Supreme', 'Roma']
	return render_template('index.html', f_name = first_name, f_pizza = favorite_pizza)

#Create about page
@app.route('/about')
def about():
	return render_template('about.html')