#!/usr/bin/env bash

bash ../structure_prediction/unpack_pdb_files.sh ./test_data

bash ../structure_prediction/extract_alpha_carbon_coordinate_info.sh ./extracted_test_data

bash ../structure_prediction/remove_empty_files.sh ./extracted_test_data
#
#echo Preparing distance adjacency matrix. This will take some time...
#python3 ./structure_prediction/create_adjacency_matrix.py -o $2
#echo Distance maps created
#
#echo Merging with amino acid features. This could stake some time....
#python3 ./structure_prediction/merge_aaFeatures_adjacency_matrix.py -o $2
#echo Merge completed
#
## Create the output folder and transfer files there
#mkdir ./output
#cd output && mkdir ./adjacency_matrix
#mkdir ./final_features
#mkdir ./pickle
#
#cd ../$2
#mv adjacency*.csv ../output/adjacency_matrix
#mv *.npy ../output/final_features
#mv *_label ../output/pickle
#mv *_feature ../output/pickle
#cd ../
#rm -rf ./$2
#rm -rf ./extracted_data
#
#conda deactivate
#
#echo All files have been processed
#echo
#echo Script completed. You can now start training the model.
