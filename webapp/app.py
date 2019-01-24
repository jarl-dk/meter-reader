#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/billeder')
def billeder():
    file_names = []
    with os.scandir('/home/toke/Pictures') as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                file_names.append(entry.name)
    return render_template('billeder.html', html_file_names=file_names)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

