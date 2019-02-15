from flask import Flask
from flask import render_template, flash, redirect, g
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
import parse_incorp
import sqlite3

class MyForm(Form):
    flodata = StringField('FLO Data', validators=[DataRequired()])

class ReportError(Form):
    comments = StringField('Comments', widget=TextArea())

conn = sqlite3.connect('errors.db')
conn.execute('''CREATE TABLE IF NOT EXISTS errorlogs (id INTEGER PRIMARY KEY AUTOINCREMENT, flodata TEXT, comments TEXT);''')
conn.close()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Teega'


@app.route("/", methods=['GET', 'POST'])
def textparse():
    form = MyForm()
    errorform = ReportError()

    if form.validate_on_submit():
        g.parsed_data = parse_incorp.parse_flodata(form.flodata.data)
        return render_template('index.html', form=form, parsed_data= g.parsed_data, errorform=errorform)

    if errorform.validate_on_submit():
        #conn = sqlite3.connect('test.db')
        #sqlquery = 'INSERT INTO errorlogs (flodata, comments) VALUES ({},{})'.format( g.parsed_data['flodata'], errorform.comments.data)
        #conn.execute(sqlquery)
        print(g.parsed_data)
        #conn.close()
        return render_template('index.html', form=form, parsed_data= g.parsed_data, errorform=errorform)

    return render_template('index.html', form=form, errorform=errorform)

app.run(debug=True)

