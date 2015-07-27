# device is the cyanogenmod codename for the device
# eg mako = Nexus 4
%define device aries
# vendor is used in device/%vendor/%device/
%define vendor sony

# Manufacturer and device name to be shown in UI
%define vendor_pretty Sony
%define device_pretty Xperia Z3 Compact


%include rpm/droid-hal-device.inc
