from flask import Flask
appp = Flask(__name__)

@appp.route('/')

def sayHi():
    return "Hello"
