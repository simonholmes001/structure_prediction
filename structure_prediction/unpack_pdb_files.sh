#!/usr/bin/env bash

# Script to unpack the PDB.cif.gz files

#echo $*

cd ./$*
pwd # in /structure_prediction/data
for dir in */
do
    echo $dir
    cd ${dir}
    pwd # in structure_prediction/data/10 etc
    for file in ./*
    do
        echo $file
        gzip -d ${file}
    done
    for cif in ./*
    do
        echo $cif
        mv $cif ../
    done
    cd ../
done
pwd # in /structure_prediction/data

mkdir extracted_data
mv *.cif extracted_data
mv extracted_data ../
cd ../
rm -rf $*
pwd # in /structure_prediction/
