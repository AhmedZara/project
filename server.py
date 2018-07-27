from flask import Flask, request, jsonify, render_template, url_for
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

def onLED(pin):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)
	return 'LED no: {} ON'.format(str(pin))

def offLED(pin):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	return 'LED no: {} OFF'.format(str(pin))


# Route "/" -> GET -> templates/led.html => Display Button for on-off & ask for pin number from the user. 
# Route "/on" -> POST => Get the pin and on or off led using RPI.
# Route "/off" -> POST => Get the pin and on or off led using RPI.
@app.route("/", methods=["GET"])
def led():
	if request.method == 'GET':
		return render_template('led.html', mode=GPIO.getmode())

@app.route("/pin_on", methods=["POST"])
def led_on():
	if request.method == 'POST':
		body = request.get_json()
		onLED(int(body.get('led')))
		return jsonify({"status": body})

@app.route("/pin_off", methods=["POST"])
def led_off():
	if request.method == 'POST':
		body = request.get_json()
		offLED(int(body.get('led')))
		return jsonify({"status":body})


@app.route("/cleanup", methods=["POST"])
def cleanup():
	if request.method == 'POST':
		GPIO.cleanup()
		return jsonify({"status": "Done cleaning the house!"})

# Route "/pwm" -> GET -> templates/pwm.html => Display Button for on-off & ask for pin number & duty cycle from the user. 
# Route "/pwm" -> POST => Get the pin & duty cycle, on or off led using RPI and then change the intensity of light.

@app.route("/pwm", methods=["GET"])
def pwm():
	if request.method == 'GET':
		return render_template('pwm.html',mode=GPIO.getmode())

@app.route("/pwmon", methods=["POST"])
def pwmon():
	if request.method == 'POST':
		body = request.get_json()
		GPIO.setup(int(body.get('led')),GPIO.OUT)
		p=GPIO.PWM(int(body.get('led')),50)
		p.start(0)

		try:
			while True:
				for i in range(100):
					p.ChangeDutyCycle(i)
            		time.sleep(1)
        		for i in range(100):
        			p.ChangeDutyCycle(100-i)
        			time.sleep(1)

		except keyboardInterrupt:
			pass


		p.stop()
		GPIO.cleanup()
		return jsonify({"status": body}) 


		

# Route "/traffic" -> GET -> templates/traffic.html => Display Button for on-off & ask for pin number 
# Route "/traffic" -> POST => Get the pin  on or off led using RPI


@app.route("/traffic", methods=["GET"])
def traffic():
	if request.method == 'GET':
		return render_template('traffic.html', mode=GPIO.getmode())

@app.route("/redpin_on", methods=["POST"])
def redpin_on():
	if request.method == 'POST':
		body = request.get_json()
		onLED(int(body.get('led')))
		return jsonify({"status": body})

@app.route("/redpin_off", methods=["POST"])
def redpin_off():
	if request.method == 'POST':
		body = request.get_json()
		offLED(int(body.get('led')))
		return jsonify({"status":body})

@app.route("/yellowpin_on", methods=["POST"])
def yellowpin_on():
	if request.method == 'POST':
		body = request.get_json()
		onLED(int(body.get('led')))
		return jsonify({"status": body})

@app.route("/yellowpin_off", methods=["POST"])
def yellowpin_off():
	if request.method == 'POST':
		body = request.get_json()
		offLED(int(body.get('led')))
		return jsonify({"status":body})

@app.route("/greenpin_on", methods=["POST"])
def greenpin_on():
	if request.method == 'POST':
		body = request.get_json()
		onLED(int(body.get('led')))
		return jsonify({"status": body})

@app.route("/greenpin_off", methods=["POST"])
def greenpin_off():
	if request.method == 'POST':
		body = request.get_json()
		offLED(int(body.get('led')))
		return jsonify({"status":body})

# Route "/pattern" -> GET -> templates/pattern.html => Display Button for on-off & ask for pin number 
# Route "/pattern" -> POST => Get the pin  on or off led using RPI

@app.route("/pattern", methods=["GET"])
def pattern():
	if request.method == 'GET':
		return render_template('traffic.html', mode=GPIO.getmode())

@app.route("/pattern_on", methods=["POST"])
def pattern_on():
	if request.method == 'POST':
		body = request.get_json()
		for i in range(0,5):
			onLED(int(body.get('led1')))
			onLED(int(body.get('led6')))
			time.sleep(3)

			offLED(int(body.get('led1')))
			offLED(int(body.get('led6')))
			time.sleep(0.5)

			onLED(int(body.get('led2')))
			onLED(int(body.get('led5')))
			time.sleep(2)

			offLED(int(body.get('led2')))
			offLED(int(body.get('led5')))
			time.sleep(0.5)

			onLED(int(body.get('led3')))
			onLED(int(body.get('led4')))
			time.sleep(3)

			offLED(int(body.get('led3')))
			offLED(int(body.get('led4')))
			time.sleep(0.5)
		return jsonify({"status": body})
 



if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')