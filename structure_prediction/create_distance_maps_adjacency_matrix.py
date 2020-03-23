import os
import pandas as pd
import numpy as np
import scipy
from scipy.spatial import distance

W_PATH = '../coordinate_data'


class CreateDistanceMapsAdjacencyMatrix:

    def __init__(self, walk_path):
        self.walk_path = walk_path

    def extract_critical_information(self):
        """Converts .cif to .csv with only essential information"""
        for root, dirs, files in os.walk(self.walk_path, topdown=False):
            for name in files:
                with open(self.walk_path + '/' + name.split('.')[0] + '.cif') as infile:
                    target_list = infile.read().split('\n')
                    df = pd.DataFrame(data=target_list, columns=["header"])  # Put list in a dataframe m X 1 column
                    df_2 = df.header.str.split(expand=True)  # Put dataframe to m x 20 columns
                    df_3 = df_2.drop(columns=[0, 2, 3, 4, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20],
                                     axis=1)  # Remove non essential columns
                    return df_3.to_csv(self.walk_path + '/' + name.split('.')[0] + '.csv', encoding='utf-8', index=False,
                                header=False)

    def calculate_distance_maps(self):
        """Creates the distance maps"""
        filenames = []
        for root, dirs, files in os.walk(self.walk_path, topdown=False):
            for name in files:
                if '.csv' in name:
                    filenames.append(name)

        for name in filenames:
            read_csv_df = pd.read_csv(self.walk_path + '/' + name, header=None)
            read_csv_less_df = read_csv_df[:-1]
            remove_columns_df = read_csv_less_df.drop(columns=[0, 1], index=1)
            convert_to_array = remove_columns_df.to_numpy()
            calculate_distances = distance.pdist(convert_to_array, 'euclidean')
            make_square = distance.squareform(calculate_distances)
            to_df_for_saving = pd.DataFrame(make_square)
            return to_df_for_saving.to_csv(self.walk_path + '/2_' + name, encoding='utf-8', index=False, header=False)

    def join_datasets(self):
        """Combines the datasets"""
        filenames_2 = []
        for root, dirs, files in os.walk(self.walk_path, topdown=False):
            for name in files:
                if '2_' in name:
                    filenames_2.append(name)

        for name in filenames:
            for name_2 in filenames_2:
                df_1 = pd.read_csv(self.walk_path + '/' + name_2, header=None)
                df_2 = pd.read_csv(self.walk_path + '/' + name, header=None)
                df_join = pd.concat([df_2, df_1], axis=1, join='inner')  # Join the databases
                return df_join.to_csv(self.walk_path + '/COMPLETE_' + name, encoding='utf-8', index=False, header=False)

def main():
    CreateDistanceMapsAdjacencyMatrix(W_PATH)

if __name__ == '__main__':
    main()
