'''
Created on Sep 8, 2018

@author: K3NN!
'''
from flask import Flask
app = Flask(__name__)
@app.route("/")

def index():
    return "Hello World"
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)
