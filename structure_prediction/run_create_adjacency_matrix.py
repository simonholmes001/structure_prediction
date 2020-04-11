import os
import argparse
from tqdm import tqdm
from create_adjacency_matrix import CreateAdjacencyMatrix

parser = argparse.ArgumentParser(description='To set W_PATH to the same directory that contains the coordinate data extracted from the pdb.cif files')
parser.add_argument('-o', '--output_directory', help='An output directory must be named', required=True)

args = parser.parse_args()

W_PATH = args.output_directory

def main(W_PATH):
    for root, dirs, files in os.walk('./' + W_PATH, topdown=False):
        for name in tqdm(files):
            with open('./' + W_PATH + '/' + name) as infile:
                target_list = infile.read().split('\n')
                di = CreateAdjacencyMatrix(W_PATH, name.split('_')[0], target_list)
                di.prepare_adjaceny_matrix(target_list)
                di.create_distance_matrix()
                di.convert_to_tensor()
                di.save_label_tensor()
                di.save_amino_acid_tags()

if __name__ == '__main__':
    main(W_PATH)
