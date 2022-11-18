from flask import Flask, render_template, request
from datetime import date, time, datetime
from unicorn_helpers import test_flash
from chrono import Chrono

app = Flask(__name__)


# @app.route('/')
# def index():
#     return "Hello World"
clock = Chrono(19, 0, 8, 0)
clock.tick()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/flash')
def flash():
    test_flash()
    return render_template('flash.html')


@app.route('/time')
def get_time():
    # right_now=datetime.now().strftime("%b-%d-%Y, %H:%M:%s")
    right_now = f'{clock.current_hour}:{clock.current_min}:{clock.current_sec}'
    return render_template('time.html', time=right_now)


@app.route('/bedtime')
def bedtime():
    def convert_num(n):
        return str(n)
    bedtime_hour = (clock.bedtime // 60)
    bedtime_min = (clock.bedtime % 60)
    return render_template('bedtime.html', bedtime_display=f'{bedtime_hour}:{bedtime_min}')


@app.route('/change_bedtime', methods= ["POST", "GET"])
def change_bedtime():
    if request.method == 'GET':
        return f'Try using "/bedtime"'
    if request.method == "POST":
        form_data = request.form
        hour = int(form_data["hour"])
        minute = int(form_data["minute"])
        response = clock.change_bedtime(hour, minute)
        return response["message"]


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
