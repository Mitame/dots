#!/bin/bash
set -e
timefile=$(dirname $0)/timefile



$(dirname $0)/output.sh stop

rm $timefile
