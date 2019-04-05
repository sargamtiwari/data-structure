# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:49:53 2019

@author: NED2KOR
"""


from flask import Flask, jsonify
app=Flask(__name__)
@app.route("/")
def hello():
    pridiction=[123.566,155.122,678.89]
    return jsonify({pridiction})
if __name__=='__main__' :
    app.run()