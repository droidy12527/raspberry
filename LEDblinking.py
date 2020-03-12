import RPi.GPIO as GPIO
import time
import picamera
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from email.mime.image import MIMEImage

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
         
        fromaddr = "hackerbadshah1010@gmail.com"    # change the email address accordingly
        toaddr = "gundiaramasu@gmail.com"
         
        mail = MIMEMultipart()
         
        mail['From'] = fromaddr
        mail['To'] = toaddr
        mail['Subject'] = "Attachment"
        body = "Please find the attachment"

        def sendMail(data):
            mail.attach(MIMEText(body, 'plain'))
            print data
            dat='%s.jpg'%data
            print dat
            attachment = open(dat, 'rb')
            image=MIMEImage(attachment.read())
            attachment.close()
            mail.attach(image)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "xdahackeranddeveloper")
            text = mail.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()

        def capture_image():
            data= time.strftime("%d_%b_%Y|%H:%M:%S")
            camera.start_preview()
            time.sleep(5)
            print data
            camera.capture('%s.jpg'%data)
            camera.stop_preview()
            time.sleep(1)
            sendMail(data)

        camera.rotation=180
        camera.awb_mode= 'auto'
        camera.brightness=55
        capture_image()
        time.sleep(1)
                
                
                
