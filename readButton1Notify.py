import struct
import sys
import bluepy.btle as btle

class MyDelegate(btle.DefaultDelegate):
    #Constructor (run once on startup)  
    def __init__(self, params):
        btle.DefaultDelegate.__init__(self)
      
    #func is caled on notifications
    def handleNotification(self, cHandle, data):
         print ("Notification from Handle: 0x" + format(cHandle,'02X') + " Value: "+ format(ord(data[0])))
      
# Initialisation  -------
if len(sys.argv) != 2:
  print "Fatal, must pass device address:", sys.argv[0], "<device address="">"
  quit()

p = btle.Peripheral(sys.argv[1],"random")
p.setDelegate( MyDelegate(p) )

# Turn notifications on
p.writeCharacteristic(0xf, struct.pack('<bb', 0x01, 0x00))

# Main loop --------
while True:
    if p.waitForNotifications(1.0):
        # handleNotification() was called
        continue

    print "Waiting... Waited more than one sec for notification"
    # Perhaps do something else here
