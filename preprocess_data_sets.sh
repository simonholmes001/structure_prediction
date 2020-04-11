#!/usr/bin/env bash

# Script to prepare data from the downloaded PDB for the structure_prediction project

KEY=c

echo Starting...
mkdir data
echo Loading data sets 0 to 9
echo Loading Data 0...
cp -r /media/simon/disk/protein_folding/test_data/g0 data
sleep 5
echo Loading Data 1...
cp -r /media/simon/disk/protein_folding/test_data/g1 data
sleep 5
echo Loading Data 2...
cp -r /media/simon/disk/protein_folding/test_data/g2 data
sleep 5
echo Loading Data 3...
cp -r /media/simon/disk/protein_folding/test_data/g3 data
sleep 5
echo Loading Data 4...
cp -r /media/simon/disk/protein_folding/test_data/g4 data
sleep 5
echo Loading Data 5...
cp -r /media/simon/disk/protein_folding/test_data/g5 data
sleep 5
echo Loading Data 6...
cp -r /media/simon/disk/protein_folding/test_data/g6 data
sleep 5
echo Loading Data 7...
cp -r /media/simon/disk/protein_folding/test_data/g7 data
sleep 5
echo Loading Data 8...
cp -r /media/simon/disk/protein_folding/test_data/g8 data
sleep 5
echo Loading Data 9...
cp -r /media/simon/disk/protein_folding/test_data/g9 data
sleep 5

echo Running script...
bash -i create_datasets.sh data holding
sleep 5
echo Transfer data to external drives...
echo Transferring amino acid tags...
cp output/final_features/*amino* /media/simon/disk/protein_folding/amino_acid_tags/
sleep 5
echo Transferring pickle files...
cp output/pickle/* /media/simon/disk/protein_folding/pickle_files/
sleep 5

echo Starting data sets a to j

mkdir data
echo Loading DataSet a...
cp -r /media/simon/disk/protein_folding/test_data/ga data
sleep 5
echo Loading DataSet b...
cp -r /media/simon/disk/protein_folding/test_data/gb data
sleep 5
echo Loading DataSet c...
cp -r /media/simon/disk/protein_folding/test_data/gc data
sleep 5
echo Loading DataSet d...
cp -r /media/simon/disk/protein_folding/test_data/gd data
sleep 5
echo Loading DataSet e...
cp -r /media/simon/disk/protein_folding/test_data/ge data
sleep 5
echo Loading DataSet f...
cp -r /media/simon/disk/protein_folding/test_data/gf data
sleep 5
echo Loading DataSet g...
cp -r /media/simon/disk/protein_folding/test_data/gg data
sleep 5
echo Loading DataSet h...
cp -r /media/simon/disk/protein_folding/test_data/gh data
sleep 5
echo Loading DataSet i...
cp -r /media/simon/disk/protein_folding/test_data/gi data
sleep 5
echo Loading DataSet j...
cp -r /media/simon/disk/protein_folding/test_data/gj data
sleep 5

echo Running scripts...
bash -i create_datasets.sh data holding
sleep 5
echo Transfer data to external drives...
echo Transferring amino_acid_tags
cp output/final_features/*amino* /media/simon/disk/protein_folding/amino_acid_tags/
sleep 5
echo Transferring pickle_files
cp output/pickle/* /media/simon/disk/protein_folding/pickle_files/
sleep 5

echo Starting DataSets k to s

mkdir data
echo Loading DataSet k...
cp -r /media/simon/disk/protein_folding/test_data/gk data
sleep 5
echo Loading DataSet l...
cp -r /media/simon/disk/protein_folding/test_data/gl data
sleep 5
echo Loading DataSet m...
cp -r /media/simon/disk/protein_folding/test_data/gm data
sleep 5
echo Loading DataSet n...
cp -r /media/simon/disk/protein_folding/test_data/gn data
sleep 5
echo Loading DataSet o...
cp -r /media/simon/disk/protein_folding/test_data/go data
sleep 5
echo Loading DataSet p...
cp -r /media/simon/disk/protein_folding/test_data/gp data
sleep 5
echo Loading DataSet q...
cp -r /media/simon/disk/protein_folding/test_data/gq data
sleep 5
echo Loading DataSet r...
cp -r /media/simon/disk/protein_folding/test_data/gr data
sleep 5
echo Loading DataSet s...
cp -r /media/simon/disk/protein_folding/test_data/gs data
sleep 5

echo Running scripts...
bash -i create_datasets.sh data holding
sleep 5
echo Transfer data to external drives
echo Transferring amino_acid_tags
cp output/final_features/*amino* /media/simon/disk/protein_folding/amino_acid_tags/
sleep 5
echo Transferring pickle_files
cp output/pickle/* /media/simon/disk/protein_folding/pickle_files/
sleep 5

echo Starting DataSets t to z

mkdir data
echo Loading DataSet t...
cp -r /media/simon/disk/protein_folding/test_data/gt data
sleep 5
echo Loading DataSet u...
cp -r /media/simon/disk/protein_folding/test_data/gu data
sleep 5
echo Loading DataSet v...
cp -r /media/simon/disk/protein_folding/test_data/gv data
sleep 5
echo Loading DataSet w...
cp -r /media/simon/disk/protein_folding/test_data/gw data
sleep 5
echo Loading DataSet x...
cp -r /media/simon/disk/protein_folding/test_data/gx data
sleep 5
echo Loading DataSet y...
cp -r /media/simon/disk/protein_folding/test_data/gy data
sleep 5
echo Loading DataSet z...
cp -r /media/simon/disk/protein_folding/test_data/gz data
sleep 5

echo Running scripts...
bash -i create_datasets.sh data holding
sleep 5

echo Transfer data to external drives...
echo Transferring amino_acid_tags
cp output/final_features/*amino* /media/simon/disk/protein_folding/amino_acid_tags/
sleep 5
echo Transferring pickle_files
cp output/pickle/* /media/simon/disk/protein_folding/pickle_files/
sleep 5

echo Script completed
