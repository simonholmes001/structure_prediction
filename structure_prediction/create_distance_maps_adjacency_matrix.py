import os
import pandas as pd
import numpy as np
import scipy
from scipy.spatial import distance
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser(description='To set W_PATH to the same directory that contains the coordinate data extracted from the pdb.cif files')
parser.add_argument('-o', '--output_directory', help='An output directory must be named', required=True)

args = parser.parse_args()

W_PATH = args.output_directory
cif_names = []
filenames = []
filenames_2 = []


class CreateDistanceMapsAdjacencyMatrix:

    def __init__(self, walk_path, cif_names, filenames, filenames_2):
        self.walk_path = walk_path
        self.cif_names = cif_names
        self.filenames = filenames
        self.filenames_2 = filenames_2

    def prepare_filenames(self, *args):
        print("Preparing file name lists for later use...")
        for Count, Item in enumerate(args):
            if Item == 'cif_names':
                for root, dirs, files in os.walk('./' + self.walk_path, topdown=False):
                    for name in files:
                        cif_names.append(name)
            elif Item == 'filenames':
                for root, dirs, files in os.walk('./' + self.walk_path, topdown=False):
                    for name in files:
                        if '.csv' in name:
                            filenames.append(name)
            elif Item == 'filenames_2':
                for root, dirs, files in os.walk('./' + self.walk_path, topdown=False):
                    for name in files:
                        if '2_' in name:
                            filenames_2.append(name)
        print("Preparation complete")

        return self.cif_names, self.filenames, self.filenames_2

    def extract_critical_information(self, cif_names):
        """Converts .cif to .csv with only essential information"""
        print("Extract coordinate information from pdb.cif files, saving as pdb.csv...")
        for name in self.cif_names:
            with open('./' + self.walk_path + '/' + name) as infile:
                target_list = infile.read().split('\n')
                df = pd.DataFrame(data=target_list, columns=["header"])  # Put list in a dataframe m X 1 column
                df = df[:-1] # Delete last row of the dataframe which has been added in line above
                df_2 = df.header.str.split(expand=True)  # Put dataframe to m x 20 columns
                df_3 = df_2.drop(columns=[0, 2, 3, 4, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20],
                                 axis=1)  # Remove non essential columns
                df_3.to_csv('./' + self.walk_path + '/' + name.split('.')[0] + '.csv', encoding='utf-8', index=False,
                            header=False)
        print("Extraction complete")

    def calculate_distance_maps(self, filenames):
        """Creates the distance maps"""
        print("Preparing distance maps...")
        for name in self.filenames:
            read_csv_df = pd.read_csv('./' + self.walk_path + '/' + name, header=None)
            read_csv_less_df = read_csv_df[:-1] # remove last row of the dataframe
            remove_columns_df = read_csv_less_df.drop(columns=[0, 1], axis=1)
            convert_to_array = remove_columns_df.to_numpy()
            calculate_distances = distance.pdist(convert_to_array, 'euclidean')
            make_square = distance.squareform(calculate_distances)
            to_df_for_saving = pd.DataFrame(make_square)
            to_df_for_saving.to_csv('./' + self.walk_path + '/2_' + name, encoding='utf-8', index=False, header=False)
        print("Distance maps completed")

    def join_datasets(self, filenames, filenames_2):
        """Combines the datasets"""
        print("Join datasets")
        for name in tqdm(self.filenames):
            for name_2 in self.filenames_2:
                df_1 = pd.read_csv('./' + self.walk_path + '/' + name_2, header=None)
                df_2 = pd.read_csv('./' + self.walk_path + '/' + name, header=None)
                df_join = pd.concat([df_2, df_1], axis=1, join='inner')  # Join the databases
                df_join.to_csv('./' + self.walk_path + '/COMPLETE_' + name, encoding='utf-8', index=False, header=False)
        print("Process complete")

def main():
    create_maps = CreateDistanceMapsAdjacencyMatrix(args.output_directory, cif_names, filenames, filenames_2)
    create_maps.prepare_filenames('cif_names')
    create_maps.extract_critical_information(cif_names)
    create_maps.prepare_filenames('filenames')
    create_maps.calculate_distance_maps(filenames)
    create_maps.prepare_filenames('filenames_2')
    create_maps.join_datasets(filenames, filenames_2)

if __name__ == '__main__':
    main()
