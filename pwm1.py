from flask import Flask, request, jsonify, render_template, url_for
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

@app.route("/pwm", methods=["GET"])
def pwm():
	if request.method == 'GET':
		return render_template('pwm.html',mode=GPIO.getmode())

@app.route("/pwmon", methods=["POST"])
def pwmon():
	if request.method == 'POST':
		body = request.get_json()
		GPIO.setup(int(body.get('led')),GPIO.OUT)
		p=GPIO.PWM(int(body.get('led')),100)
		p.start(0)

		try:
			while True:
				for i in range(50):
					p.ChangeDutyCycle(i)
            		time.sleep(0.1)
        		for i in range(50):
        			p.ChangeDutyCycle(50-i)
        			time.sleep(0.1)

		except keyboardInterrupt:
			pass


		p.stop()
		return jsonify({"status": body}) 
