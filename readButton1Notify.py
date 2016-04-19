import struct
import sys
from bluepy.btle import UUID, Peripheral,DefaultDelegate

class MyDelegate(DefaultDelegate):
    #Constructor (run once on startup)  
    def __init__(self, params):
        DefaultDelegate.__init__(self)
      
    #func is caled on notifications
    def handleNotification(self, cHandle, data):
         print ("Notification from Handle: 0x" + format(cHandle,'02X') + " Value: "+ format(ord(data[0])))
      
# Initialisation  -------
button_service_uuid = UUID(0xA000)
button_char_uuid    = UUID(0xA001)

if len(sys.argv) != 2:
  print "Fatal, must pass device address:", sys.argv[0], "<device address="">"
  quit()

p = Peripheral(sys.argv[1],"random")
p.setDelegate( MyDelegate(p) )

#Get ButtonService
ButtonService=p.getServiceByUUID(button_service_uuid)
# Get The Button-Characteristics
ButtonC=ButtonService.getCharacteristics(button_char_uuid)[0]
#Get The handle tf the  Button-Characteristics
hButtonC=ButtonC.getHandle()
# Search and get Get The Button-Characteristics "property" (UUID-0x2902 CCC-Client Characteristic Configuration))
#  wich is located in a handle in the range defined by the boundries of the ButtonService
for desriptor in p.getDescriptors(hButtonC,0x00F):  # The handle range should be read from the services 
   if (desriptor.uuid == 0x2902):                   #      but is not done due to a Bluez/BluePy bug :(     
        print ("Button1 Client Characteristic Configuration found at handle 0x"+ format(desriptor.handle,"02X"))
        hButtonCCC=desriptor.handle
 
# Turn notifications on by setting bit0 in the CCC more info on:
# https://developer.bluetooth.org/gatt/descriptors/Pages/DescriptorViewer.aspx?u=org.bluetooth.descriptor.gatt.client_characteristic_configuration.xml    
p.writeCharacteristic(hButtonCCC, struct.pack('<bb', 0x01, 0x00))
print "Notification is turned on for Button1"

# Main loop --------
while True:
    if p.waitForNotifications(1.0):
        # handleNotification() was called
        continue

    print "Waiting... Waited more than one sec for notification"
    # Perhaps do something else here
