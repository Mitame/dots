#!/usr/bin/env python3

import time
import sys
from stem import CircStatus
from stem.control import Controller, EventType
from pprint import pprint
from inspect import getmembers

# Get the connection with some error handling
try:
    controller = Controller.from_port()
except:
    print("Could not connect to tor.")
    sys.exit(1)

try:
    controller.authenticate()
except:
    print("Could not authenticate with tor.")
    sys.exit(1)

circuits = {}

for circuit in controller.get_circuits():
    circuits[circuit.id] = circuit

def on_circuit_change(event):
    global circuits

    circuits[event.id] = event
#    print(event.status, event.purpose)
    show_status()

def show_status():
    global circuits

    best_connection = 0
    for circuit in circuits.values():
        if circuit.status in (CircStatus.BUILT, CircStatus.EXTENDED):
            if best_connection < 2:
                best_connection = 2
                break
        elif circuit.status in (CircStatus.CLOSED, CircStatus.FAILED):
            # if best_connection
            pass
        else:
            if best_connection < 1:
                best_connection = 1
    colours = {
        "tor": "#ff1700",
        "vpn": "#ff1700",
        "wireless": "#ff1700",
        "ethernet": "#ff1700"
    }
    if best_connection == 2:
        colours["tor"] = "#0bd800"
    elif best_connection == 1:
        colours["tor"] = "#ff9300"
    else:  # best_connection == 0
        colours["tor"] = "#ff1700"

    print(("%{{F{vpn}}}V" +
           "%{{F{ethernet}}}E" +
           "%{{F{wireless}}}W" +
           "%{{F{tor}}}T" +
           "%{{F-}}").format(**colours))
          
    sys.stdout.flush()


# print(controller.get_version())

controller.add_event_listener(on_circuit_change, EventType.CIRC)

try:
    while True:
        show_status()
        time.sleep(60)
except KeyboardInterrupt:
    controller.close()
    sys.exit(0)
