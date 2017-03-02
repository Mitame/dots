#!/bin/bash
set -e
timefile=$(dirname $0)/timefile

if [[ -f ${timefile} ]]
then
  seconds=$(( $(date +%s) - $(cat $timefile) - (60*60)))

  hms=$(date --date="@${seconds}" +%H:%M:%S)

  if [[ "${1}" == "stop" ]]
  then
    echo -n "%{F#0bd800}${hms}%{F-}"
  else
    echo -n "%{F-}${hms}%{F-}"
  fi
else
  echo -n "  TiMER "
fi
