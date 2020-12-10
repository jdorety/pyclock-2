from flask import Flask, render_template
from datetime import date, time, datetime
from unicorn_helpers import test_flash
from chrono import Chrono

app = Flask(__name__)


# @app.route('/')
# def index():
#     return "Hello World"
time = Chrono()
time.tick()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/flash')
def flash():
    test_flash()
    return render_template('flash.html')


@app.route('/time')
def get_time(time=datetime.now().strftime("%b-%d-%Y, %H:%M")):
    return render_template('time.html', time=time)


@app.route('/config')
def config_clock(hour=time.current_hour, min=time.current_min):
    return render_template('config.html', hour=hour, min=min)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
