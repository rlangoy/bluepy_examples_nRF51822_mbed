# bluepy examples using nRF51822 width mbed

This rspository contain examples on how to use bluepy to comminicate width the nRF51-DK(nRF51822 Development kit) using mbed<br>

The nRF51-DK is programmed using the mbed templates found on https://developer.mbed.org/<br>
The used templates is:  <br>
* [BLE_Button Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_Button/?platform=Nordic-nRF51-DK)
    * Uses an BLE/GATT input characteristic: read-only, boolean, with notifications. The characteristic is updated according to a single button's state.
* [BLE_LED    Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_LED/?platform=Nordic-nRF51-DK)
    * Uses an BLE/GATT output characteristic:read-write, boolean. The characteristic is used to control of a single LED.
    

bluepy Installation on Raspberry pi3 
------------------------------------
Other raspberryes or PC's width a BLE usb dongle running the Debian "Jessie" image might work :smiley:<br><br>
Check the curent linux distro. 
* cat /etc/os-release  

Install [BlueZ] (http://www.bluez.org)  - The Official Linux Bluetooth protocol stack
* sudo apt-get install bluez

Install [bluepy] (http://ianharvey.github.io/bluepy-doc) - Python interface to Bluetooth LE on Linux
* sudo apt-get install python-pip libglib2.0-dev
* sudo pip install bluepy

Downloaing the the bluepy example files
----------------------------------------
*  git clone https://github.com/rlangoy/bluepy_examples_nRF51822_mbed.git

File information
----------------
blesca.py - runs a LE device scan. The file originates form the [bluepy doc's] (http://ianharvey.github.io/bluepy-doc/scanner.html#sample-code)
Using the bluepy examples
-------------------------
Change the dictory to the one width the example files
* cd bluepy_examples_nRF51822_mbed/
Start by discover your BLE devices by running
* sudo python blesca.py

Expected output:
```text
Device 08:df:1f:c4:30:69 (public), RSSI=-98 dB
  Flags = 12
  Complete 16b Services = befe
  Manufacturer = 0033400a0100
Device c7:db:9e:41:3f:c8 (random), RSSI=-97 dB
  Flags = 06
  Complete 16b Services = edfe
Device 46:10:30:d8:24:8e (random), RSSI=-101 dB
  Flags = 1a
Device 00:22:d0:34:d1:e9 (public), RSSI=-97 dB
  Complete Local Name = Polar Loop 34D1E91B
  Flags = 05
Device 7a:bd:a3:c2:cb:e3 (random), RSSI=-101 dB
  Flags = 1a
Device f9:ee:30:21:f6:6d (random), RSSI=-31 dB
  Flags = 06
  Complete 16b Services = 00a0
  Complete Local Name = Button
Device 61:dc:cf:ee:64:08 (random), RSSI=-98 dB
  Flags = 1a
  Manufacturer = 4c000100002000000000000000000000000000
```

