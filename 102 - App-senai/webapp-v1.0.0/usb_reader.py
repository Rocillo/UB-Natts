import usb.core 
import usb.util 
import time 
import requests 
import json 
import RPi.GPIO as GPIO 
 
USB_IF      = 0 # Interface 
USB_TIMEOUT = 5 # Timeout in MS 
USB_VENDOR  = 0x1c34 # Vendor-ID:  
USB_PRODUCT = 0x7241 # Product-ID 
 
# Find the HID device by vender/product ID
dev = usb.core.find(idVendor=USB_VENDOR, idProduct=USB_PRODUCT) 
 
# Get and store the endpoint 
endpoint = dev[0][(0,0)][0] 
 
if dev.is_kernel_driver_active(USB_IF) is True: 
    dev.detach_kernel_driver(USB_IF) 
 
# Claim the device 
usb.util.claim_interface(dev, USB_IF) 

# Configure the Raspberry Pi GPIO
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(11, GPIO.OUT) 
 
receivedNumber = 0 
while True: 
    control = None 
     
    try: 
        # Read a character from the device 
        control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
        
        # Here you have to analyze what's coming in.
        # In my case you had to check the first byte (command)
        if control[0] == 2:
            # Convert ascii to a number, there's probably better ways to do so.
            receivedDigit = control[2] - 29 
        
            if receivedDigit == 10: 
                receivedDigit = 0
                
            # Append the digit to the number
            receivedNumber = 10 * receivedNumber + receivedDigit 
        
        # Check if the received character is CRLF
        if (( control[0] == 0 )) & (( control[2] == 40 )) & (( not receivedNumber == 0 )): 
            resp = requests.post("http://127.0.0.1/verify-access.php",data={'cardNumber':receivedNumber});
            print "card: " + str(receivedNumber)             
            ret_data = json.loads(resp.text) 
            print ret_data["message"] 
            print ret_data["can_enter"] 
            if ret_data["can_enter"] == "1":
                print "student: " + ret_data["student"]
                
                # Start the machine
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(1) 
                GPIO.output(11, GPIO.LOW) 
            print 
            receivedNumber = 0 
    except KeyboardInterrupt: 
        GPIO.cleanup() 
    except: 
        pass 
     
    time.sleep(0.001) # Let CTRL+C actually exit 