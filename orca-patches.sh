#!/bin/bash -i

echo " === Syncing repos ==="

git fetch orca
git fetch me

git reset --hard orca/main

echo " === Apply patches ==="

# Current pull requests

# My changes
gc-series orca/main..me/docker
gc-series orca/main..me/build-changes
gc-series orca/main..me/my-changes
