from flask_restful import Resource
from flask import render_template, session, flash, request


class LogSummary(Resource):
    def get(self):
        if not session.get('logged_in'):
            return render_template('login.html')
        else:
            return 'Great !!'
        pass

    def login(self):
        if request.form['password'] == 'passowrd' and request.form['username'] == 'admin':
            session['logged_in'] = True
        else:
            flash('Wrong Password !!')
        return self.get()