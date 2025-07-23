#!/bin/bash

curl -k "$1" | sed 's/pgStoryZeroJSON = //p;d' | sed 's/;*$//' | read-pg.py | more
