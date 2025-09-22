#!/bin/bash

perl -pi -e 's/^M190 S[0-9]* ; set bed temperature and wait for it to be reached$//' "$1"
perl -pi -e 's/^G10 S[0-9]* ; set nozzle temperature$//' "$1"
