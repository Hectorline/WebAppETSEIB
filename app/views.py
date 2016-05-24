from flask import render_template
from app import app
from flask import request
import csv

from app.scripts.calculs import matriculats,aprovats,percentatge,notamitja,llistamitja,llistapercent 

	
@app.route('/')
@app.route('/index')
def index():
		return render_template('index.html')

				
@app.route("/filtre", methods=['POST'])
def filtre():
		# aprov = [49.9, 71.5, 6.4, 29.2, 44.0, 76.0, 35.6, 48.5, 16.4, 94.1]
    percent = [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3]
    c = request.form['curs']
    q = request.form['quad']
    s = request.form['gender']
    aprov = llistamitja(c,q,s)
    percent = llistapercent(c,q,s)
    return render_template('grafics2016-2.html',aprov=aprov,percent=percent,curs=c,quad=q,sexe=s)
if __name__ == '__main__':
	app.run()
