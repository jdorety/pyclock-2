from flask import Flask
import time
import unicornhat

app = Flask(__name__)


# @app.route('/')
# def index():
#     return "Hello World"


@app.route('/')
def flash():
    unicornhat.set_pixel(0, 0, 255, 255, 255)
    unicornhat.show()
    unicornhat.clear()
    unicornhat.show()
    return "That did it!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
