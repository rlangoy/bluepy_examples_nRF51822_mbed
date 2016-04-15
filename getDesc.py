import sys
from bluepy.btle import UUID, Peripheral

if len(sys.argv) != 2:
  print "Fatal, must pass device address:", sys.argv[0], "<device address="">"
  quit()

p = Peripheral("f9:ee:30:21:f6:6d","random")

c=p.getDescriptors(1,0x0f)
for i in c:
   print i
