from flask import Flask, render_template, request
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
def get_time():
    # right_now=datetime.now().strftime("%b-%d-%Y, %H:%M:%s")
    right_now = f'{time.current_hour}:{time.current_min}:{time.current_sec}'
    return render_template('time.html', time=right_now)


@app.route('/bedtime')
def bedtime():
    def convert_num(n):
        return str(n)
    convert_bedtime = map(convert_num, time.bedtime)
    bedtime_string = ":".join(convert_bedtime)
    return render_template('bedtime.html', bedtime_display=bedtime_string)


@app.route('/change_bedtime', methods= ["POST", "GET"])
def change_bedtime():
    print(request.method)
    print(request.form)
    if request.method == 'GET':
        return f'Try using "/bedtime"'
    if request.method == "POST":
        form_data = request.form
        hour = int(form_data["hour"])
        minute = int(form_data["minute"])
        response = time.change_bedtime(hour, minute)
        return response.message


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
