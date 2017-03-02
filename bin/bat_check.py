#!/usr/bin/env python3
from pydbus import SystemBus, SessionBus
from gi.repository import GLib
import os
import sys
import datetime

system_bus = SystemBus()
CORRECT_SERIAL = "3552"
try:
    display_device = system_bus.get(".UPower", "/org/freedesktop/UPower/devices/battery_BAT1")
except ArithmeticError:
    sys.exit(1)


serial = display_device.Get("org.freedesktop.UPower.Device", "Serial")

if CORRECT_SERIAL != serial:
    session_bus = SessionBus()
    notification = session_bus.get(".Notifications", "/org/freedesktop/Notifications")

    notification.Notify(
        "Battery Checker",
        0,
        "battery-full-symbolic",
        "Battery not valid",
        "The battery has been replaced with a fake\n%s != %s" % (CORRECT_SERIAL, serial),
        [],
        {},
        -1
    )
