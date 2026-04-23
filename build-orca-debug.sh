#!/bin/bash

if [ ! -d deps/build-dbginfo ]; then
  ./build_linux.sh -j4 -d
fi

./build_linux.sh -j4 -esr
