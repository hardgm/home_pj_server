from flask import Flask, render_template
import lgpio

app = Flask(__name__)

@app.route('/')
def hello_user():
    return render_template('led_on_off.html')

@app.route('/led/on')
def led_on():
    handle = lgpio.gpiochip_open(0)
    lgpio.gpio_claim_output(handle, 22)
    lgpio.gpio_write(handle, 22, 1)
    lgpio.gpiochip_close(handle)
    return 'LED ON'

@app.route('/led/off')
def led_off():
    handle = lgpio.gpiochip_open(0)
    lgpio.gpio_claim_output(handle, 22)
    lgpio.gpio_write(handle, 22, 0)
    lgpio.gpiochip_close(handle)
    return 'LED OFF'


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')