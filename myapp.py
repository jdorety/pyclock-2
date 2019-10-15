from flask import Flask, render_template
from datetime import date, time, datetime
from unicorn_helpers import test_flash
import clock

app = Flask(__name__)


# @app.route('/')
# def index():
#     return "Hello World"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/flash')
def flash():
    test_flash()
    return render_template('flash.html')


@app.route('/time')
def get_time(time=datetime.now().strftime("%b-%d-%Y, %H-%M")):
    return render_template('time.html', time=time)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
