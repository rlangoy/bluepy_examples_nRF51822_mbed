import sys
import binascii
import struct
import time
from bluepy.btle import UUID, Peripheral

button_service_uuid = UUID(0xa001)

if len(sys.argv) != 2:
  print "Fatal, must pass device address:", sys.argv[0], "<device address="">"
  quit()

p = Peripheral(sys.argv[1], "random")

try:
    ch = p.getCharacteristics(uuid=button_service_uuid)[0]
    if (ch.supportsRead()):
        while 1:
            val = binascii.b2a_hex(ch.read())
            print ("0x" + val)
            time.sleep(1)

finally:
    p.disconnect()
