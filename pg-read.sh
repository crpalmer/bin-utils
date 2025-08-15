#!/bin/bash

curl -k "$1" | sed 's/pgStoryZeroJSON = //p;d' | sed 's/;*$//' | tee /tmp/pg-read.tmp | _pg-read.py | less
