#!/bin/bash

# Script to extract alpha-Carbon coordinates from the PDB.cif files

echo $*
mkdir ./$*

cd ./extracted_data

list="$(find . -name '*.cif')"
for file in $list
do
	TARGET=$(echo "${file##*/}")
	grep "^ATOM.*CA\|^MODEL" ${TARGET} > ../$*/$TARGET
done
