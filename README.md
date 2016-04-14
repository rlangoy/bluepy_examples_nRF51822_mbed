# bluepy examples using nRF51822 width mbed

This rspository contain examples on how to use bluepy to comminicate width the nRF51-DK(nRF51822 Development kit) using mbed<br>

The nRF51-DK is programmed using the mbed templates found on https://developer.mbed.org/<br>
The used templates is:  <br>
* [BLE_Button Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_Button/?platform=Nordic-nRF51-DK)
    * Uses an BLE/GATT input characteristic: read-only, boolean, with notifications. The characteristic is updated according to a single button's state.
* [BLE_LED    Example](https://developer.mbed.org/teams/Bluetooth-Low-Energy/code/BLE_LED/?platform=Nordic-nRF51-DK)
    * Uses an BLE/GATT output characteristic:read-write, boolean. The characteristic is used to control of a single LED.
    

bluepy Installation
--------------------
On Raspberry pi3 (or other raspberryes width BLE usb dongle) running the "Raspbian Jessie" image
* run cat /etc/os-release to display your version :smiley:

Install [BlueZ] (http://www.bluez.org) (The Official Linux Bluetooth protocol stack)
* sudo apt-get install bluez

Install [bluepy] (http://ianharvey.github.io/bluepy-doc) Python interface to Bluetooth LE on Linux
* sudo apt-get install python-pip libglib2.0-dev
* sudo pip install bluepy
