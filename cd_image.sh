#!/bin/sh

for file in *; do
	grep "../../image" ${file}
    # sed -i 's|../image|../../image|g' ${file}
done