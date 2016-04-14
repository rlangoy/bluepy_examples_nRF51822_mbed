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
blesca.py - runs a LE device scan. The file originates form the [bluepy doc's] (http://ianharvey.github.io/bluepy-doc/scanner.html#sample-code)<br>
getDeviceName.py - displays [gap Device Name] (https://developer.bluetooth.org/gatt/characteristics/Pages/CharacteristicViewer.aspx?u=org.bluetooth.characteristic.gap.device_name.xml)<br>
readButton1.py - displays the button1 value (UUID 0xa001 - Custom Service) from the  [BLE_Button Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_Button/?platform=Nordic-nRF51-DK)
 

Using the bluepy examples
-------------------------
Change the dictory to the one width the example files
* cd bluepy_examples_nRF51822_mbed

#####blesca.py
--------------
Start by discover your BLE devices by running
* sudo python blesca.py

Expected output when the nRF51-dk is programmed using the [BLE_Button Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_Button/?platform=Nordic-nRF51-DK)
```text
Device f9:ee:30:21:f6:6d (random), RSSI=-31 dB
  Flags = 06
  Complete 16b Services = 00a0
  Complete Local Name = Button
```

#####getDeviceName.py
---------------------
Display your BLE [ Device Name] (https://developer.bluetooth.org/gatt/characteristics/Pages/CharacteristicViewer.aspx?u=org.bluetooth.characteristic.gap.device_name.xml) by running:
* python getDeviceName.py xx:xx:xx:xx:xx:xx 
   *   Where the xx:xx:xx:xx:xx:xx is the MAC address that could be found by running the blesca.py 
      * The MAC address for my device is f9:ee:30:21:f6:6d   :smiley: 

<br> Expected output is:
```text
nRF5x
```
#####readButton1.py
---------------------
Displays the button1 value (UUID 0xa001 - Custom Service) from the  [BLE_Button Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_Button/?platform=Nordic-nRF51-DK) by running:
* python readButton1.py xx:xx:xx:xx:xx:xx 

The program polls the "Button Service" (UUID 0xa001) every second and displays the "Button1" state:
* value 0x00 button not pushed
* value 0x01 button pushed

