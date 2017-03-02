#!/usr/bin/env python3
import time
import sys

i = 0

while 1:
    sys.stdout.write("Testing %i\n" % i)
    sys.stdout.flush()
    time.sleep(1)
    i += 1
