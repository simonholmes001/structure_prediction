import os
import pandas as pd
import numpy as np
from tqdm import tqdm
import argparse
import torch
import pickle

parser = argparse.ArgumentParser(description='To set W_PATH to the same directory that contains the coordinate data extracted from the pdb.cif files')
parser.add_argument('-o', '--output_directory', help='An output directory must be named', required=True)

args = parser.parse_args()

W_PATH = args.output_directory
data = {0:["ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY", "HIS", "ILE", "LEU",
           "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL"],
        'CID':[5950, 6322, 6267, 5960, 5862, 5961, 33032, 750, 6274, 6306, 6106, 5962,
               6137, 6140, 614, 5951, 6288, 6305, 6057, 6287]}
amino_acids_df = pd.DataFrame.from_dict(data)
amino_acids_df.rename(columns={0:'amino_acid_label'}, inplace=True)
standardised_features_df = pd.read_csv('./standardised_features.csv')

class MergeAAFeatures:

    def __init__(self, walk_path, amino_acids_df, standardised_features_df):
        self.walk_path = walk_path
        self.amino_acids_df = amino_acids_df
        self.standardised_features_df = standardised_features_df

    def merge_features(self):

        for root, dirs, files in os.walk('./' + self.walk_path, topdown=False):
            for name in tqdm(files):
                if 'adjacency' in name:
                    adjacency_matrix_df = pd.read_csv('./' + self.walk_path +'/' + name, header=None)
                    adjacency_matrix_df.rename(columns={0:'amino_acid_label'}, inplace=True)
                    protein_tags_df = pd.DataFrame(data=adjacency_matrix_df['amino_acid_label']) # Create a dataset of the protein's primary sequence
                    merge_amino_acids_and_features = pd.merge(self.amino_acids_df, self.standardised_features_df, on='CID', how='left')  # Join the databases
                    merge_amino_acids_and_features.drop(columns=['CID'], axis=1, inplace=True) # Remove potential duplicate columns for next step
                    merge_features_and_protein_tag = pd.merge(protein_tags_df, merge_amino_acids_and_features, on='amino_acid_label', how='left')  # Join the databases

                    # Convert to numpy arrays, pytorch tensor & save numpy & pickle

                    # Adjacency matrix
                    adjacency_to_array = adjacency_matrix_df.drop(columns=['amino_acid_label'], axis=1).to_numpy() # Convert to numpy array
                    adjacency_to_tensor = torch.from_numpy(adjacency_to_array) # Convert to pytorch tensor
                    with open('./' + self.walk_path + '/' + name.split('_')[2].split('.')[0] + '_label', 'wb') as file:
                        pickle.dump(adjacency_to_tensor, file) # Save as a pickle object
                    np.save('./' + self.walk_path + '/' + name.split('_')[2].split('.')[0] + '_adjacency', adjacency_to_array) # Save numpy array


                    # Amino acid labels
                    protein_tag_to_array = protein_tags_df.to_numpy()
                    np.save('./' + self.walk_path + '/' + name.split('_')[2].split('.')[0] + '_amino_acid_tag', protein_tag_to_array)

                    # Amino acid features
                    features_to_array = merge_features_and_protein_tag.drop(columns=['amino_acid_label'], axis=1).to_numpy()
                    features_to_tensor = torch.from_numpy(features_to_array) # Convert to pytorch tensor
                    with open('./' + self.walk_path + '/' + name.split('_')[2].split('.')[0] + '_feature', 'wb') as file:
                        pickle.dump(features_to_tensor, file) # Save as a pickle object
                    np.save('./' + self.walk_path + '/' + name.split('_')[2].split('.')[0] + '_features', features_to_array)


def main():
    merge = MergeAAFeatures(args.output_directory, amino_acids_df, standardised_features_df)
    merge.merge_features()

if __name__ == '__main__':
    main()
