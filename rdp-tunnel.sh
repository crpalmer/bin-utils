#!/bin/bash

host=home.crpalmer.org
if [ $# -eq 1 ]
then
   host="$1"
fi

echo "Connecting to: $host"
ssh "$host" -p 222 -L *:3389:192.168.1.21:3389 -N
