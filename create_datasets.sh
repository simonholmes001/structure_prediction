#!/usr/bin/env bash

# Script to prepare data for protein folding prediction studies

# Check for required arguments
if [ $# -ne 2 ]; then
    echo "usage: $0 You must enter the folder name of the pdb data AND the location of the coordinate files as arguments" 1>&2
    echo Exiting script...
    exit 1
fi

# Preparation of a virtual environment
# Commented out when running massive batch processing
echo Creating virtual environment for data preparation...
ENV=$(cat ./environment.yml | grep name | cut -f 2 -d ':')
conda update -n base conda # to update to latest version of conda
conda remove --name $ENV --all # to remove any previously installed environments called $ENV
conda activate base
conda env create -f environment.yml
conda activate $ENV
echo Virtual environment ready

rm -rf ./$2
rm -rf ./extracted_data
rm -rf ./output # Commented out when running large batch transfers as use /output/ folder in background tasks

echo Preparing to unpack files...
bash ./structure_prediction/unpack_pdb_files.sh $1 # to unpack the pdf.cif.gz files & put all unpacked pdb.cif files in a folder called extracted_data/
echo Unpacking completed

echo Preparing to extract alpha C info...
bash ./structure_prediction/extract_alpha_carbon_coordinate_info.sh $2 # to extract alpha-C coordinate information from the pdf.cif files in the extracted_data/ folder & to put them in the $2/ folder
echo Extraction complete

echo Deleting any empty coordinate files, DNA / RNA files as an example...
bash ./structure_prediction/remove_empty_files.sh $2
echo Clean-up completed

echo Preparing distance adjacency matrix. This will take some time...
python3 ./structure_prediction/run_create_adjacency_matrix.py -o $2
echo Distance maps created

echo Merging with amino acid features. This could stake some time....
python3 ./structure_prediction/merge_aaFeatures_adjacency_matrix.py -o $2
echo Merge completed

# Create the output folder and transfer files there
mkdir ./output # Commented out when running large batch transfers as use /output/ folder in background tasks
cd output && mkdir ./adjacency_matrix
mkdir ./final_features
mkdir ./pickle

cd ../$2
mv *adjacency*.csv ../output/adjacency_matrix
mv *amino*.csv ../output/final_features
mv *.npy ../output/final_features
mv *_label* ../output/pickle
mv *_feature* ../output/pickle
cd ../
rm -rf ./$2
rm -rf ./extracted_data

conda deactivate

echo All files have been processed
echo
echo Script completed. You can now start training the model.
