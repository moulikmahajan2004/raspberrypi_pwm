from gpiozero import DistanceSensor, PWMOutputDevice
from time import sleep
#GPIO PIN DEFINES
Trig_Pin = 17  
Echo_Pin = 18 
Buzzer_Pin= 27  
#max_distance=1.0 is another argument passed to the DistanceSensor constructor. 
#It specifies the maximum distance that the sensor should measure. 
#In this case, it's set to 1.0, which suggests that the sensor is configured to measure distances up to 1 meter.
ULTRASONIC_SENSOR = DistanceSensor(trigger=Trig_Pin, echo=Echo_Pin, max_distance=1.0)
buzzer = PWMOutputDevice(Buzzer_Pin)

##TRY AND EXCEPT BLOCK IS USED TO HANDEL THE EXCEPTION
try:
    while True: 
        #SLEEP IS USED TO ADD THE DELAY TO THE CODE BY 0.8 SECOND
        sleep(0.8)   
        #IT IS USED TO CALCULTE THE DISTANCE IN CM AS IT IS 
        #THE CONVERSION OF METERE FROM CENTIMETERE
        DISTANCE =ULTRASONIC_SENSOR.distance * 100 
        #PRINTING THE DISTANCE
        print("Distance (CM): %.2f" %DISTANCE) 
        #CALCULATING THE VALUE OF THE BUZZ
        #HERE THE DISTANCE IS THE VALUE WHICH IS IN CM 
        #BUZZER VALUE DEPEND ON THE VALUE OF THE ULTRASONIC SENSOR
        BUZZ=  1.0 - (DISTANCE / 100)
        print("Buzz: %.2f" % BUZZ)
        buzzer.value = BUZZ
except KeyboardInterrupt:
        #KEYBOARD INTERRUPT IS USED TO CATCH THE EXCEPTION WHEN USER 
        #PRESS THE 
    print("Program Ended") 
