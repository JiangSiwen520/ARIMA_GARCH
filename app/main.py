from flask import Flask


import pandas as pd
app = Flask(__name__)     #实例化一个Flask对象


@app.route('/')
def hello_world():
    return 'Hello, Welcome to CloudBase_JSW, 2023-02-13!!!->2023.5.1\n'
@app.route('/new')
def fun2():
    try:
        df = pd.read_excel('000001.xlsx')
    except:
        continue
    return 'Hello, Welcome to CloudBase_JSW, 2023-02-13!!!->2023.5.2\n'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)



