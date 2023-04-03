#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2023 hp_carrot.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: demo/d_flask.py
Author: hanjiatong@hp_carrot.com
Date: 2023/04/03 16:27:37
"""
import sys, os
sys.path.append(os.path.dirname(os.getcwd()))

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process', methods=['POST'])
def process():
    input_text = request.form['input_text']
    # 在这里可以对input_text进行处理
    output_text = input_text.upper()
    return render_template('result.html', output_text=output_text)

@app.route('/wait')
def wait():
    return render_template('home_wait.html')

@app.route('/process_wait', methods=['POST'])
def process_wait():
    input_text = request.form['input_text']
    # 在这里可以对input_text进行处理
    output_text = input_text.upper()
    import time
    time.sleep(10)
    return render_template('result.html', output_text=output_text)

if __name__ == '__main__':
    app.run(debug=True)

