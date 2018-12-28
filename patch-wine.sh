#!/bin/bash

scriptdir="$(dirname "$0")"
cd "$scriptdir"
export SCRIPTDIR="$PWD"

wineRootToPatch="$1"
[ "$wineRootToPatch" = "" ] && exit 1
 
rm -rf "/tmp/winebuild-dosbox" 2> /dev/null

cd "$wineRootToPatch/bin" 
mv "wine" "wine.real"

cp "$SCRIPTDIR"/bin/wine* ./
cp "$SCRIPTDIR"/bin/dosbox-wrapper* ./

cp -r "$SCRIPTDIR"/share/* "$wineRootToPatch/share/"