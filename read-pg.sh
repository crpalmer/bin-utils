#!/bin/bash

curl -k "$1" | sed 's/pgStoryZeroJSON = //p;d' | sed 's/;*$//' | tee /tmp/read-pg.tmp | read-pg.py | less
