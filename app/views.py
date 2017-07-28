from flask import render_template
from app import app
from flask import request

from app.scripts.calculs import llistamitja, llistapercent


@app.route('/')
@app.route("/", methods=['POST'])
def index():
    if request.method != 'POST':
        return render_template('index.html')
    else:
        c = request.form['curs']
        q = request.form['quad']
        s = request.form['gender']
        aprov = llistamitja(c, q, s)
        percent = llistapercent(c, q, s)
        return render_template('grafics2016-2.html', aprov=aprov, percent=percent, curs=c, quad=q, sexe=s)


if __name__ == '__main__':
    app.run()
