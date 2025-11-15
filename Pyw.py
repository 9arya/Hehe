from flask import Flask as fl

a = fl(__name__)

@a.route('/')
def id():
  return '<h1>"ajajaj"<h1>'
  
a.run()