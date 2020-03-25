import os
import pandas as pd
from tqdm import tqdm
import argparse

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
                    merge_amino_acids_and_features = pd.merge(self.amino_acids_df, self.standardised_features_df, on='CID', how='left')  # Join the databases
                    merge_amino_acids_and_features.drop(columns=['CID'], axis=1, inplace=True)
                    merge_features_and_adjacency = pd.merge(adjacency_matrix_df, merge_amino_acids_and_features, on='amino_acid_label', how='left')  # Join the databases
                    merge_features_and_adjacency.to_csv('./' + self.walk_path + '/FINAL_' + name, encoding='utf-8', index=False, header=False)

def main():
    merge = MergeAAFeatures(args.output_directory, amino_acids_df, standardised_features_df)
    merge.merge_features()

if __name__ == '__main__':
    main()
