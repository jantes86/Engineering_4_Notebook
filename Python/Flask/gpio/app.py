from flask import Flask, render_template, request 
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	if request.method == "POST":
		option = request.form.get("submitBtn")
		if option == "LED1ON":
			GPIO.output(17, GPIO.HIGH)
		if option == "LED2ON":
			GPIO.output(18, GPIO.HIGH)
		if option == "LED1OFF":
			GPIO.output(17, GPIO.LOW)
		if option == "LED2OFF":
			GPIO.output(18, GPIO.LOW)
	return render_template("index.html",)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
