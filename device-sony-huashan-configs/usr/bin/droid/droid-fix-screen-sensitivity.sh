#!/bin/sh
#
# This makes the wonky touch less wonky and less sensitive

echo 100 > /sys/devices/i2c-3/3-0024/main_ttsp_core.cyttsp4_i2c_adapter/finger_threshold
echo 0 > /sys/devices/i2c-3/3-0024/main_ttsp_core.cyttsp4_i2c_adapter/signal_disparity
