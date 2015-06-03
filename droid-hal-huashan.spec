%define device huashan
%define vendor sony

%define vendor_pretty Sony
%define device_pretty Xperia SP (C5303)


%define android_config \
#define QCOM_HARDWARE 1\
%{nil}


%include rpm/droid-hal-device.inc
