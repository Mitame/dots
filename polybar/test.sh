#!/usr/bin/env bash
i=1
while true
do
  echo "%{F#5e81b1}%{F-} ${i}%"
  i=$((i + 1))
  sleep 1
done
