import pimodule as pi
import datetime
import time

pi.init(music=False, vision=False)

def main():
    time.sleep(0) # Start
    
    pi.CAR.set_tilt(30)
    
    for _ in range(10):
        print(pi._picar.ultrasonic.read())
        time.sleep(0.2)
        
    time.sleep(1)
    pi.CAR.set_tilt(30)
    
    time.sleep(0)  # End
    
    
    
if __name__ == "__main__":
    print(f"[{datetime.datetime().strftime('%Y-%m-%d %I:%M %p')}] start: ", pi, f">>> {__name__}")
    main()
