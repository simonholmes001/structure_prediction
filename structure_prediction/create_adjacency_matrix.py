import pandas as pd
from scipy.spatial import distance
import torch
import pickle

class CreateAdjacencyMatrix:

    def __init__(self, walk_path, name, target_list):
        self.walk_path = walk_path
        self.name = name
        self.target_list = target_list

    def prepare_adjaceny_matrix(self, target_list):
        self.df_1 = pd.DataFrame(data=self.target_list, columns=["header"])  # Put list in a dataframe m X 1 column
        self.df_1 = self.df_1[:-1] # Removes additional row that is included
        self.cif_to_df_2 = self.df_1.header.str.split(expand=True)  # Put dataframe to m x 20 columns
        self.critical_info_to_df_3 = self.cif_to_df_2.drop(columns=[0, 1, 2, 3, 4, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20], axis=1)  # df containing aa & coordinate positions
        self.amino_acid_tags_df = self.critical_info_to_df_3[5]
        self.convert_to_array = self.critical_info_to_df_3.drop(columns=[5], axis=1).to_numpy() # Removes aa flag & contains only coordinate info
        return self.convert_to_array, self.amino_acid_tags_df

    def create_distance_matrix(self):
        try:
            self.calculate_distances = distance.pdist(self.convert_to_array, 'euclidean')
            self.make_square = distance.squareform(self.calculate_distances)
        except:
            pass
        try:
            return self.make_square
        except:
            pass
        # adjacency_matrix_df_4 = pd.DataFrame(make_square)
        # adjacency_matrix_df_4.to_csv('./' + self.walk_path  + '/' + name.split('.')[0] + '_adjacency_matrix_' + '.csv', encoding='utf-8', index=False, header=False)
        # adjacency_to_array = adjace ncy_matrix_df_4.to_numpy() # Convert to numpy array

    def convert_to_tensor(self):
        try:
            self.adjacency_to_tensor = torch.from_numpy(self.make_square) # Convert to pytorch tensor
        except:
            pass
        try:
            return self.adjacency_to_tensor
        except:
            pass

    def save_label_tensor(self):
        try:
            with open('./' + self.walk_path + '/' + self.name.split('.')[0] + '_label.pickle', 'wb', buffering=500000000) as file:
                pickle.dump(self.adjacency_to_tensor, file, protocol=4) # Save as a pickle object
        except:
            pass
        # np.save('./' + self.walk_path + '/' + name.split('.')[0] + '_adjacency', adjacency_to_array) # Save numpy array

    def save_amino_acid_tags(self):
        try:
            self.amino_acid_tags_df.to_csv('./' + self.walk_path + '/' + self.name.split('.')[0] + '_amino_acid_tag_' + '.csv', encoding='utf-8', index=False, header=False)
        except:
            pass

                # df_join = pd.concat([critical_info_to_df_3, adjacency_matrix_df_4], axis=1, join='inner')  # Join the databases
                # assert adjacency_matrix_df_4.shape[0] == df_join.shape[0]
                # df_join_2 = df_join.drop(columns=[10, 11, 12], axis=1) # Remove original coordinate information
                # assert df_join.shape[0] == df_join_2.shape[0]

# def main():
#     adj_mat = CreateAdjacencyMatrix(args.output_directory)
#     adj_mat.adjaceny_matrix()
#
# if __name__ == '__main__':
#     main()
