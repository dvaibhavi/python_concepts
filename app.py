from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():

    return '''<form method="POST"> 
   <centre> <input type="text" name="input_value">
    <input type="submit" value="submit"> </centre>
    </form>'''
   # return "Hello World"


@app.route('/', methods = ['POST'])
def process_input():
    input_text = request.form['input_value']
    return f'input value is : {input_text}'


if __name__ == "main":
    app.run()