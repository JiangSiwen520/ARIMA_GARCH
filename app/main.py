from flask import Flask


from test import route_test
app = Flask(__name__)     #实例化一个Flask对象
app.register_blueprint(route_test,url_prefix='/test')

@app.route('/')
def hello_world():
    return 'Hello, Welcome to CloudBase_JSW, 2023-02-13!!!->2023.5.1\n'
@app.route('/new')
def fun2():
    #df = pd.read_excel('000001.xlsx')
    return 'Hello, Welcome to CloudBase_JSW, 2023-02-13!!!->2023.5.2\n'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)



