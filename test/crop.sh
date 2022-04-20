#!/bin/sh

rm -rf cropped 
mkdir cropped
for f in *.jpg; do
    convert "$f" -crop 1440x1080+200+0 cropped/"$f" 
done
