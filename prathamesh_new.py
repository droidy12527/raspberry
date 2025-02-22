import pyrebase
import time
import RPi.GPIO as GPIO
import picamera

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

TRIG = 24
ECHO = 23
BUZZER = 27
LED = 17

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

def upload_cloud(data):
	config = {
	    "apiKey": "AIzaSyCsRnBbJru3Jg5crfEkJnpvFvSlzWJatWc",
    	"authDomain": "intuderdetector.firebaseapp.com",
    "databaseURL": "https://intuderdetector.firebaseio.com",
    "projectId": "intuderdetector",
    "storageBucket": "intuderdetector.appspot.com",
    "messagingSenderId": "834194595303",
    "appId": "1:834194595303:web:d5bcdd3c6de997f7f7f142
	}
	folder_name = time.strftime("%d-%m-%Y")
	file_name = data
	print(file_name+' '+ folder_name + ' was sucessfully uploaded')
	prath = pyrebase.initialize_app(config)
	storage = prath.storage()
	path_cloud = folder_name+"/"+file_name+".jpg"
	path_local = file_name+".jpg"
	storage.child(path_cloud).put(path_local)


def led_light():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED, GPIO.LOW)
    
def buzzer_light():
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(BUZZER, GPIO.LOW)
   
def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG,False) 

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()
        
    sig_time = end-start
    distance = sig_time / 0.000058
    print('Distance: {} cm'.format(distance))
    return distance
while True:
    distance = get_distance()
    camera = picamera.PiCamera()
    time.sleep(0.05)
    if distance <15:
        def capture_image():
            data= time.strftime("%H-%M")
            camera.start_preview()
            time.sleep(5)
            print data
            camera.capture('%s.jpg'%data)
            camera.stop_preview()
            time.sleep(1)
           upload_cloud(data) 
        camera.rotation=180
        camera.awb_mode= 'auto'
        camera.brightness=55
        capture_image()
        time.sleep(1)
                
                
                
