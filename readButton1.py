import binascii
import struct
import time
from bluepy.btle import UUID, Peripheral

button_service_uuid = UUID(0xa001)

p = Peripheral("F9:EE:30:21:F6:6D", "random")

try:
    ch = p.getCharacteristics(uuid=button_service_uuid)[0]
    if (ch.supportsRead()):
        while 1:
            val = binascii.b2a_hex(ch.read())
            print ("0x" + val)
            time.sleep(1)

finally:
    p.disconnect()
