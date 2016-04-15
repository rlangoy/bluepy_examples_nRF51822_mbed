import sys
from bluepy.btle import UUID, Peripheral

if len(sys.argv) != 2:
  print "Fatal, must pass device address:", sys.argv[0], "<device address="">"
  quit()

p = Peripheral(sys.argv[1],"random")

services=p.getServices()

#displays all services
for service in services:
   print service
