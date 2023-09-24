from flask import Flask, redirect, render_template, request, url_for, jsonify, session
import numpy as np


app = Flask(__name__)

#home page
@app.route('/', methods=['POST','GET'])
def index(): 
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)