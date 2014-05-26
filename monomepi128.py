import serial
import time
import binascii

# Hex values
LED_ON_CMD = '20'
LED_OFF_CMD = '30'
KEY_DN = '00'
KEY_UP = '10'
CLEAR_CMD = '9'
LED_ROW_CMD = '4'
LED_COL_CMD = '5'

ser = serial.Serial('COM6', 115200)

cmd = '110102'
ser.write(binascii.unhexlify(cmd))
print "Ahoy"
time.sleep(1)


ser.write(binascii.unhexlify('12'))
ser.close()
