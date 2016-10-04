# bluepy examples using nRF51822 width mbed

This rspository contain examples on how to use bluepy to comminicate width the nRF51-DK(nRF51822 Development kit) using mbed<br>

The nRF51-DK is programmed using the mbed templates found on https://developer.mbed.org/<br>
The used templates is:  <br>
* [BLE_Button Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_Button/?platform=Nordic-nRF51-DK)
    * Uses an BLE/GATT input characteristic: read-only, boolean, with notifications. The characteristic is updated according to a single button's state.
* [BLE_LED    Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_LED/?platform=Nordic-nRF51-DK)
    * Uses an BLE/GATT output characteristic:read-write, boolean. The characteristic is used to control of a single LED.
    
Requirements
--------------
The examples uses the libraries BlueZ and blueyp and was tested width:<br>
* BlueZ Version: 5.23-2+rpi1
   * Installed version could be displayed by running: dpkg --status bluez | grep '^Version:'
* bluepy Version: 1.0.4
   * Installed version could be displayed by running: pip show bluepy 

bluepy Installation on Raspberry pi3 
------------------------------------
Bluetooth installation on RPIv3 run:
```text
sudo apt-get install --no-install-recommends Bluetooth
sudo apt-get install pi-bluetooth
sudo reboot
```

Other raspberryes or PC's width a BLE usb dongle running the Debian "Jessie" image might work :smiley:<br><br>
Check the curent linux distro. 
* cat /etc/os-release  

Install [BlueZ] (http://www.bluez.org)  - The Official Linux Bluetooth protocol stack
```text
sudo apt-get install bluez
```
Install [bluepy] (http://ianharvey.github.io/bluepy-doc) - Python interface to Bluetooth LE on Linux
```text
sudo apt-get install python-pip libglib2.0-dev
sudo pip install bluepy
```
Downloaing the the bluepy example files
----------------------------------------
*  git clone https://github.com/rlangoy/bluepy_examples_nRF51822_mbed.git

File information
----------------
blesca.py - Runs a LE device scan. The file originates form the [bluepy doc's] (http://ianharvey.github.io/bluepy-doc/scanner.html#sample-code)<br>
getServices.py - Displays the device's available services <br>
getDeviceCharacteristics.py - Displays the device's characteristics-handles,-UUIDs and properties<br>
getDeviceName.py - Displays [gap Device Name] (https://developer.bluetooth.org/gatt/characteristics/Pages/CharacteristicViewer.aspx?u=org.bluetooth.characteristic.gap.device_name.xml)<br>
readButton1.py - Displays the button1 value (UUID 0xa001 - custom service) from the  [BLE_Button Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_Button/?platform=Nordic-nRF51-DK)<br>
getDesc.py - Displays the device's [discriptors](https://developer.bluetooth.org/gatt/descriptors/Pages/DescriptorsHomePage.aspx)<br>
readButton1Notify.py - Same as readButton1.py, but uses Notfication instead of polling the button1 value<br>
writeLed2.py - Turns the LED2 on/off using the [BLE_LED Example] (https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_LED/?platform=Nordic-nRF51-DK) 

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

#####getServices.py.py
----------------------
 Displays the device's Characteristics-handles,-UUIDs and properties by running :
* python getServices.py xx:xx:xx:xx:xx:xx 
   *   Where the xx:xx:xx:xx:xx:xx is the MAC address that could be found by running the blesca.py 
      * The MAC address for my device is f9:ee:30:21:f6:6d   :smiley: 

<br> Expected output when the nRF51-DK is running the [BLE_Button Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_Button/?platform=Nordic-nRF51-DK)
```text
Service <uuid=Generic Attribute handleStart=8 handleEnd=11>
Service <uuid=Generic Access handleStart=1 handleEnd=7>
Service <uuid=a000 handleStart=12 handleEnd=65535>
```
The Service UUID=0xA000 is a custom service that contain is used to display the nRF51-DK button1's state<br>
* The button1's state could be obtained by reading the value stored in the characteristics-UUID 0xA001<br> (this is a custom characteristics)

#####getDeviceCharacteristics.py
--------------------------------
Displays the Device's handles,characteristic-UUIDs and properties by running :
* python getDeviceCharacteristics.py xx:xx:xx:xx:xx:xx 

<br> Expected output when the nRF51-DK is running the [BLE_Button Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_Button/?platform=Nordic-nRF51-DK)
```text
Handle   UUID                                Properties
-------------------------------------------------------
  0x03   00002a00-0000-1000-8000-00805f9b34fb READ WRITE
  0x05   00002a01-0000-1000-8000-00805f9b34fb READ
  0x07   00002a04-0000-1000-8000-00805f9b34fb READ
  0x0A   00002a05-0000-1000-8000-00805f9b34fb INDICATE
  0x0E   0000a001-0000-1000-8000-00805f9b34fb NOTIFY READ
```
Information about the characteristic-UUID's could be found at [bluetooth.org] (https://developer.bluetooth.org/gatt/characteristics/Pages/CharacteristicsHome.aspx) <br>

The characteristic-UUID is where you could read/write values to update or get information from your BLE-device<br>

The first entry has the UUID 0x2A00 wich is defined as org.bluetooth.characteristic.gap.device_name. The content cound be displayed using getDeviceName.py

#####getDeviceName.py
---------------------
Display your BLE [ Device Name] (https://developer.bluetooth.org/gatt/characteristics/Pages/CharacteristicViewer.aspx?u=org.bluetooth.characteristic.gap.device_name.xml) by running:
* python getDeviceName.py xx:xx:xx:xx:xx:xx 

<br>
The program searches the the UUID 0x2A00  entry, wich is defined as org.bluetooth.characteristic.gap.device_name and displays its content as a string
<br> 
<br> 
Expected output when the nRF51-DK is running the [BLE_Button Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_Button/?platform=Nordic-nRF51-DK)
```text
nRF5x
```
#####readButton1.py
---------------------
Displays the button1 value (UUID 0xa001 - custom characteristics) from the  [BLE_Button Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_Button/?platform=Nordic-nRF51-DK) by running:
* python readButton1.py xx:xx:xx:xx:xx:xx 

The program  displays the "Button1" state: every second by polling the "Button1 characteristics" (UUID 0xa001) value
* value 0x00 button not pushed
* value 0x01 button pushed

<br>
*The service-UUID 0xA000 
   * contains a custom characteristics-UUID 0xA001 .A custom characteristics, means that it is not predefined in the characteristics list from  [bluetooth.org] (https://developer.bluetooth.org/gatt/characteristics/Pages/CharacteristicsHome.aspx). 
      * In plain english characteristics-UUID 0xA001 is the variable that contain the button1's state.

#####getDesc.py 
---------------
Displays the device's [discriptors](https://developer.bluetooth.org/gatt/descriptors/Pages/DescriptorsHomePage.aspx) by running:
* python getDesc.py xx:xx:xx:xx:xx:xx 

Expected output when the nRF51-DK is running the [BLE_Button Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_Button/?platform=Nordic-nRF51-DK)
```text
UUID                                  Handle UUID by name
 00002800-0000-1000-8000-00805f9b34fb  0x01   Descriptor <2800>
 00002803-0000-1000-8000-00805f9b34fb  0x02   Descriptor <2803>
 00002a00-0000-1000-8000-00805f9b34fb  0x03   Descriptor <Device Name>
 00002803-0000-1000-8000-00805f9b34fb  0x04   Descriptor <2803>
 00002a01-0000-1000-8000-00805f9b34fb  0x05   Descriptor <Appearance>
 00002803-0000-1000-8000-00805f9b34fb  0x06   Descriptor <2803>
 00002a04-0000-1000-8000-00805f9b34fb  0x07   Descriptor <Peripheral Preferred Connection Parameters>
 00002800-0000-1000-8000-00805f9b34fb  0x08   Descriptor <2800>
 00002803-0000-1000-8000-00805f9b34fb  0x09   Descriptor <2803>
 00002a05-0000-1000-8000-00805f9b34fb  0x0A   Descriptor <Service Changed>
 00002902-0000-1000-8000-00805f9b34fb  0x0B   Descriptor <Client Characteristic Configuration>
 00002800-0000-1000-8000-00805f9b34fb  0x0C   Descriptor <2800>
 00002803-0000-1000-8000-00805f9b34fb  0x0D   Descriptor <2803>
 0000a001-0000-1000-8000-00805f9b34fb  0x0E   Descriptor <a001>
 00002902-0000-1000-8000-00805f9b34fb  0x0F   Descriptor <Client Characteristic Configuration>
```
From the this list we asees that the characteristics whdth UUID=0xA001 (Button1 characteristics) has a Descriptor ("Property setting's") named "Client Characteristic Configuration" (CCC).<br>
CCC is used to enable/disable Notifications/Indications) more information is found in the following [link] (https://developer.bluetooth.org/gatt/descriptors/Pages/DescriptorViewer.aspx?u=org.bluetooth.descriptor.gatt.client_characteristic_configuration.xml) <br>
Enabling notifications for the Button1 characteristics (UUID=0xA001) is done by setting bit0 (the first bit = 1) in the CCC (Client Characteristic Configuration). The CCC is accessed by witing to the handle (0x0f).

#####readButton1Notify.py
-------------------------
Displays and enables Nortfication for changes in the button1 value (UUID 0xa001 - custom service) from the  [BLE_Button Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_Button/?platform=Nordic-nRF51-DK) by running:
* python readButton1Notify.py xx:xx:xx:xx:xx:xx 
<br> 
<br>
Expected output when the nRF51-DK is running the [BLE_Button Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_Button/?platform=Nordic-nRF51-DK)
```text
Button1 Client Characteristic Configuration found at handle 0x0F
Notification is turned on for Button1
Waiting... Waited more than one sec for notification
Notification from Handle: 0x0E Value: 1
Notification from Handle: 0x0E Value: 0
```

#####writeLed2.py
-----------------
Turns the LED2 on/off using the [BLE_LED Example] (https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_LED/?platform=Nordic-nRF51-DK)  by running:
* python writeLed2.py xx:xx:xx:xx:xx:xx 
<br> 
<br>
Expected output when the nRF51-DK is running the [BLE_LED Example] (https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_LED/?platform=Nordic-nRF51-DK)
```text
Led2 on
Led2 off
Led2 on
Led2 off
```







