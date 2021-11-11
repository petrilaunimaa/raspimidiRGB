cd /sys/kernel/config/usb_gadget/ 
mkdir -p midi_over_usb 
cd midi_over_usb 
echo 0x1d6b > idVendor # Linux Foundation 
echo 0x0104 > idProduct # Multifunction Composite Gadget 
echo 0x0100 > bcdDevice # v1.0.0 
echo 0x0200 > bcdUSB # USB2 
mkdir -p strings/0x409 
echo "fedcba9876543210" > strings/0x409/serialnumber 
echo "HTP" > strings/0x409/manufacturer 
echo "MIDI USB Device" > strings/0x409/product 
ls /sys/class/udc > UDC