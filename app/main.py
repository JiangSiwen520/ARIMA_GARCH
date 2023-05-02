from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Welcome to CloudBase_JSW, 2023-02-13!!!->2023.5.1\n'
@app.route('/new')
def fun2():
    #df = pd.read_excel('000001.xlsx')
    return 'Hello, Welcome to CloudBase_JSW, 2023-02-13!!!->2023.5.2\n'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)



