from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=''):
    return f"hello {name}"

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

@app.route('/convert/<celsius>')
def convert(celsius):
    celsius = float(celsius)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return f"<h1>{celsius}°C is {fahrenheit:.2f}°F</h1>"



if __name__ == '__main__':
    app.run()
