from flask import Blueprint
route_test = Blueprint("test_page",__name__)
@route_test('/')
def hello_world():
    return "Hello World"
@route_test('/hello')
def hello():
    return "Hello"
