import sys
import binascii
import struct
import time
from bluepy.btle import UUID, Peripheral

led_service_uuid = UUID(0xA000)
led_char_uuid = UUID(0xA001)

if len(sys.argv) != 2:
  print "Fatal, must pass device address:", sys.argv[0], "<device address="">"
  quit()

p = Peripheral(sys.argv[1], "random")
LedService=p.getServiceByUUID(led_service_uuid)

try:
    ch = LedService.getCharacteristics(led_char_uuid)[0]
    while 1:
     	ch.write(struct.pack('<B', 0x00));
      	print ("Led2 on")
     	time.sleep(1)
       	ch.write(struct.pack('<B', 0x01));
    	print ("Led2 off")
       	time.sleep(1)
finally:
    p.disconnect()
