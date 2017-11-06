from flask_restful import Resource
from flask import render_template, session, flash, request
from flask import jsonify

class LogSum(Resource):
    def get(self):
        return get_log()
        if not session.get('logged_in'):
            return render_template('login.html')
        else:
            return 'Great !!'

    def login(self):
        if request.form['password'] == 'passowrd' and request.form['username'] == 'admin':
            session['logged_in'] = True
        else:
            flash('Wrong Password !!')
        return self.get()

import datetime
def get_log(filt=None):
    count = {}
    with open('request_log.log') as f:
        lines = f.readlines()
        for line in lines:
            t = line.split('|')
            ip = t[0].strip()
            endpoint = t[1].strip()
            timestamp = t[2].strip()

            if filt is not None:
                if endpoint != filt:
                    continue

            if ip not in count:
                count[ip] = {}
            if endpoint not in count[ip]:
                count[ip][endpoint] = []
            timestamp = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S') + " UTC"
            count[ip][endpoint].append(timestamp)

    return jsonify(logset = count)