#!/bin/bash
set -e
timefile=$(dirname $0)/timefile

date +%s > $timefile

$(dirname $0)/output.sh start
