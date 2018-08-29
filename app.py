from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/flaskPostgres'
db = SQLAlchemy(app)

class Random(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	random = db.Column(db.String(100))

	def __init__(self, random):
		self.random = random

	def __repr__(self):
		return 'Random: %s' % self.random

@app.route('/')
# @app.route('/')
def home():
	return render_template('home.html')

@app.route('/random', methods=['POST'])
def random():
	random = Random(request.form['random'])
	db.session.add(random)
	db.session.commit()
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True)
	# app.run()