# device is the cyanogenmod codename for the device
# eg mako = Nexus 4
%define device aries
# vendor is used in device/%vendor/%device/
%define vendor sony

# Manufacturer and device name to be shown in UI
%define vendor_pretty Sony
%define device_pretty Xperia Z3 Compact
%define android_config \
#define QCOM_BSP 1\
%{nil}
%include rpm/droid-hal-device.inc
