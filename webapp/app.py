#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, send_from_directory

PICTURES_DIR = '/home/toke/Pictures'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/billeder/<file_name>')
def billede(file_name):
    return send_from_directory(PICTURES_DIR, file_name)



@app.route('/billeder')
def billeder():
    file_names = []
    with os.scandir(PICTURES_DIR) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                file_names.append(entry.name)
    return render_template('billeder.html', html_file_names=file_names)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

