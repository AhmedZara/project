from flask import Flask, request, jsonify, render_template, url_for #used to import functions
import RPi.GPIO as GPIO #imports RPi package from raspberry library
import time # imports time for delay 


app = Flask(__name__) #initialization of flask
GPIO.setmode(GPIO.BCM) #sets the GPIO mode (BCM-GPIO, BOARD-PIN) 

def onLED(pin): #function to ON led
    GPIO.setup(pin, GPIO.OUT) #sets the pin as OUTPUT pin
    GPIO.output(pin, GPIO.HIGH) #turns ON the lED
    return 'LED no: {} ON'.format(str(pin)) #used to display on the console window

def offLED(pin): #function to OFF led
    GPIO.setup(pin, GPIO.OUT) #sets the pin as OUTPUT pin
    GPIO.output(pin, GPIO.LOW) #turns OFF the lED
    return 'LED no: {} OFF'.format(str(pin))   #used to display on the console window


#Program to turn ON and OFF LED

@app.route("/", methods=["GET"]) 
# Route "/" -> GET -> templates/led.html => Display Button for on-off & ask for pin number from the user. 
def led():
    if request.method == 'GET':
        return render_template('led.html', mode=GPIO.getmode())

@app.route("/pin_on", methods=["POST"]) # Route "/pin_on" -> POST => Get the pin and on or off led using RPI.
def led_on():
    if request.method == 'POST':
        body = request.get_json()
        onLED(int(body.get('led'))) #calls the function 'onLED'
        return jsonify({"status": body})

@app.route("/pin_off", methods=["POST"]) # Route "/pin_off" -> POST => Get the pin and on or off led using RPI.
def led_off():
    if request.method == 'POST':
        body = request.get_json()
        offLED(int(body.get('led'))) #calls the function 'onLED'
        return jsonify({"status":body})


#Program to show Pulse width Modulation of a LED

@app.route("/pwm", methods=["GET"])
# Route "/pwm" -> GET -> templates/pwm.html => Display Button for on-off & ask for pin number from the user. 

def pwm():
    if request.method == 'GET':
        return render_template('pwm.html',mode=GPIO.getmode())

@app.route("/pwmon", methods=["POST"])
# Route "/pwmon" -> POST => Get the pin & duty cycle, on or off led using RPI and then change the intensity of light.
def pwmon():
    if request.method == 'POST':
        body = request.get_json()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(int(body.get('led')),GPIO.OUT)  #sets the pin as output
        p=GPIO.PWM(int(body.get('led')),100)   #PWM function
        p.start(0)  #starts the duty cycle at 0

        for x in range(0,5):  
            for i in range(50):
                p.ChangeDutyCycle(i) #changes duty cycle (increment)
                time.sleep(0.1) #provides a delay of 0.1 sec
            for i in range(50):
                p.ChangeDutyCycle(50-i)   #changes duty cycle (decrement)
                time.sleep(0.1)

        p.stop()
        GPIO.cleanup()
        return jsonify({"status": body})
        

        
#Program to Turn ON and OFF Multiple LEDs

@app.route("/traffic", methods=["GET"])
# Route "/traffic" -> GET -> templates/traffic.html => Display Button for on-off & ask for pin number 
def traffic():
    if request.method == 'GET':
        return render_template('traffic.html', mode=GPIO.getmode())

@app.route("/redpin_on", methods=["POST"])  # Route "/redpin_on" -> POST => Get the pin on led using RPI
def redpin_on():
    if request.method == 'POST':
        body = request.get_json()
        onLED(int(body.get('led')))  #calls the function 'onLED'
        return jsonify({"status": body})

@app.route("/redpin_off", methods=["POST"]) # Route "/redpin_off" -> POST => Get the pin off led using RPI
def redpin_off():
    if request.method == 'POST':
        body = request.get_json()
        offLED(int(body.get('led')))  #calls the function 'offLED'
        return jsonify({"status":body})

@app.route("/yellowpin_on", methods=["POST"])  # Route "/yellowpin_on" -> POST => Get the pin on led using RPI
def yellowpin_on():
    if request.method == 'POST':
        body = request.get_json()
        onLED(int(body.get('led')))  #calls the function 'onLED'
        return jsonify({"status": body})

@app.route("/yellowpin_off", methods=["POST"])  # Route "/yellowpin_off" -> POST => Get the pin off led using RPI
def yellowpin_off():
    if request.method == 'POST':
        body = request.get_json()
        offLED(int(body.get('led')))  #calls the function 'offLED'
        return jsonify({"status":body})

@app.route("/greenpin_on", methods=["POST"])  # Route "/greenpin_on" -> POST => Get the pin on led using RPI
def greenpin_on():
    if request.method == 'POST':
        body = request.get_json()
        onLED(int(body.get('led'))) #calls the function 'onLED'
        return jsonify({"status": body})

@app.route("/greenpin_off", methods=["POST"])  # Route "/greenpin_off" -> POST => Get the pin off led using RPI
def greenpin_off():
    if request.method == 'POST':
        body = request.get_json()
        offLED(int(body.get('led')))  #calls the function 'onLED'
        return jsonify({"status":body})


#Program to generate pattern (Automatic glowing of LEDs (Traffic lights))

@app.route("/pattern", methods=["GET"])
# Route "/pattern" -> GET -> templates/pattern.html => Display Button for on-off & ask for pin number 
def pattern():
    if request.method == 'GET':
        return render_template('pattern.html', mode=GPIO.getmode())

@app.route("/pattern_on", methods=["POST"])  # Route "/pattern_on" -> POST => Get the pin  on or off led using RPI
def pattern_on():
    if request.method == 'POST':
        body = request.get_json()
        for i in range(0,5):
            onLED(int(body.get('led1')))  #calls the function 'onLED'
            onLED(int(body.get('led6')))
            time.sleep(3)  #provides a delay for 3 sec

            offLED(int(body.get('led1')))  #calls the function 'onLED'
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

@app.route("/cleanup", methods=["POST"]) # Route "/cleanup" -> deletes all the data in the end 
def cleanup():
    if request.method == 'POST':
        GPIO.cleanup()
        return jsonify({"status": "Done cleaning the house!"})


if __name__ == '__main__':      #debug and run flask -> app
    app.run(debug=True, host='0.0.0.0')