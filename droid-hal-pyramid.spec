%define device pyramid
%define vendor htc

%define vendor_pretty HTC
%define device_pretty Sensation

%define android_config \
#define QCOM_BSP 1\
%{nil}

%include rpm/droid-hal-device.inc
