#!/bin/bash

sudo docker run --user `id -u`:`id -g` --rm -it -v "`pwd`":/app build-orca
