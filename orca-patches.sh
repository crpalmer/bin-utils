#!/bin/bash -i

echo " === Syncing repos ==="

git fetch orca
git fetch me
git fetch kisslorand
git fetch ianalexis

git reset --hard orca/main

echo " === Apply patches ==="

# My changes
gc-series orca/main..me/build-changes
#gc-series orca/main..me/supports
gc-series orca/main..me/my-changes
gc-series orca/main..me/extruder-variant

# Current pull requests
echo "*** WARNING *** using my rebase of kisslorand's support patches"
gc-series orca/main..me/kisslorand-supports # rebase of:
#gc-series orca/main..kisslorand/Fix-support-interface-contact-semantics-and-gap-handling    # issue 11812

#gc-series orca/main..ianalexis/waylan-bug
