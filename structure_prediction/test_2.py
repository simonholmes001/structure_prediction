import os
import pandas as pd
from scipy.spatial import distance
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser(description='To set W_PATH to the same directory that contains the coordinate data extracted from the pdb.cif files')
parser.add_argument('-o', '--output_directory', help='An output directory must be named', required=True)

args = parser.parse_args()

W_PATH = args.output_directory

with open('../coordinate_data/11gs.cif') as infile:
    target_list = infile.read().split('\n')
    df_1 = pd.DataFrame(data=target_list, columns=["header"])  # Put list in a dataframe m X 1 column
    df_1 = df_1[:-1] # Removes additional row that is included
    cif_to_df_2 = df_1.header.str.split(expand=True)  # Put dataframe to m x 20 columns
    assert df_1.shape[0] == cif_to_df_2.shape[0]
    critical_info_to_df_3 = cif_to_df_2.drop(columns=[0, 1, 2, 3, 4, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20], axis=1)  # df containing aa & coordinate positions
    assert cif_to_df_2.shape[0] == critical_info_to_df_3.shape[0]
    convert_to_array = critical_info_to_df_3.drop(columns=[5], axis=1).to_numpy() # Removes aa flag & contains only coordinate info
    calculate_distances = distance.pdist(convert_to_array, 'euclidean')
    make_square = distance.squareform(calculate_distances)
    adjacency_matrix_df_4 = pd.DataFrame(make_square)
    assert critical_info_to_df_3.shape[0] == adjacency_matrix_df_4.shape[0]
    df_join = pd.concat([critical_info_to_df_3, adjacency_matrix_df_4], axis=1, join='inner')  # Join the databases
    print(df_join.head())
    df_join_2 = df_join.drop(columns=[10, 11, 12], axis=1)
    print(df_join_2.head())
    # df_join.drop(columns=[1, 2, 3]), axis=1) # Remove original coordinate information
    # assert adjacency_matrix_df_4.shape[0] == df_join.shape[0]
    # df_join.to_csv('./' + self.walk_path + '/adjacency_matrix_' + name, encoding='utf-8', index=False, header=False)

