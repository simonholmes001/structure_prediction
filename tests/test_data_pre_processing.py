#!/usr/bin/env python

"""Tests for `pubchem_api` package."""

import os
import numpy as np
import pandas as pd
import scipy
from scipy.spatial import distance

import unittest
# from click.testing import CliRunner
# from structure_prediction import cli

class TestDataPreprocessing(unittest.TestCase):
    """Tests for `data pre-processing` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_001_adjacency_matrix_ok(self):
        """
        Tests to ensure that adjacency matrix prepared correctly
        To show that distance.pdist function calculates correctly on a simple test array
        """
        print("Test One... To show that distance.pdist function calculates correctly on a simple test array")
        test_array_1 = np.array([[1, 2, 3],
                                [4, 5, 6],
                                 [7, 8, 9],
                                 [10, 11, 12]])

        a = np.sqrt(((1-1)**2) + ((2-2)**2) + ((3-3)**2))
        b = np.sqrt(((1-4)**2) + ((2-5)**2) + ((3-6)**2))
        c = np.sqrt(((1-7)**2) + ((2-8)**2) + ((3-9)**2))
        d = np.sqrt(((1-10)**2) + ((2-11)**2) + ((3-12)**2))

        e = np.sqrt(((4-1)**2) + ((5-2)**2) + ((6-3)**2))
        f = np.sqrt(((4-4)**2) + ((5-5)**2) + ((6-6)**2))
        g = np.sqrt(((4-7)**2) + ((5-8)**2) + ((6-9)**2))
        h = np.sqrt(((4-10)**2) + ((5-11)**2) + ((6-12)**2))

        i = np.sqrt(((7-1)**2) + ((8-2)**2) + ((9-3)**2))
        j = np.sqrt(((7-4)**2) + ((8-5)**2) + ((9-6)**2))
        k = np.sqrt(((7-7)**2) + ((8-8)**2) + ((9-9)**2))
        l = np.sqrt(((7-10)**2) + ((8-11)**2) + ((9-12)**2))

        m = np.sqrt(((10-1)**2) + ((11-2)**2) + ((12-3)**2))
        n = np.sqrt(((10-4)**2) + ((11-5)**2) + ((12-6)**2))
        o = np.sqrt(((10-7)**2) + ((11-8)**2) + ((12-9)**2))
        p = np.sqrt(((10-10)**2) + ((11-11)**2) + ((12-12)**2))

        result_array = np.array([[a, b, c, d],
                                 [e, f, g, h],
                                 [i, j, k, l],
                                 [m, n, o, p]])

        print(result_array)

        calculate_distances = distance.pdist(test_array_1, 'euclidean')
        make_square = distance.squareform(calculate_distances)
        print(make_square)

        assert np.array_equal(result_array, make_square)


    def test_002_adjacency_matrix_ok(self):
        """
        Tests to ensure that adjacency matrix prepared correctly
        To show that distance.pdist function calculates correctly on a simple test array
        """

        print(("Test Two... To show that distance.pdist function calculates correctly on a simple test array"))
        test_array_1 = np.array([[1, 2, 3],
                                 [4, 5, 6],
                                 [7, 8, 9],
                                 [10, 11, 12]])

        a = np.sqrt(((1-1)**2) + ((2-2)**2) + ((3-3)**2))
        b = np.sqrt(((1-4)**2) + ((2-5)**2) + ((3-6)**2))
        c = np.sqrt(((1-7)**2) + ((2-8)**2) + ((3-9)**2))
        d = np.sqrt(((1-10)**2) + ((2-11)**2) + ((3-12)**2))

        e = np.sqrt(((4-1)**2) + ((5-2)**2) + ((6-3)**2))
        f = np.sqrt(((4-4)**2) + ((5-5)**2) + ((6-6)**2))
        g = np.sqrt(((4-7)**2) + ((5-8)**2) + ((6-9)**2))
        h = np.sqrt(((4-10)**2) + ((5-11)**2) + ((6-12)**2))

        i = np.sqrt(((7-1)**2) + ((8-2)**2) + ((9-3)**2))
        j = np.sqrt(((7-4)**2) + ((8-5)**2) + ((9-6)**2))
        k = np.sqrt(((7-7)**2) + ((8-8)**2) + ((9-9)**2))
        l = np.sqrt(((7-10)**2) + ((8-11)**2) + ((9-12)**2))

        m = np.sqrt(((10-1)**2) + ((11-2)**2) + ((12-3)**2))
        n = np.sqrt(((10-4)**2) + ((11-5)**2) + ((12-6)**2))
        o = np.sqrt(((10-7)**2) + ((11-8)**2) + ((12-9)**2))
        p = np.sqrt(((10-10)**2) + ((11-11)**2) + ((12-12)**2))

        result_array = np.array([[a, b, c, d],
                                 [e, f, g, h],
                                 [i, j, k, l],
                                 [m, n, o, p]])

        calculate_distances = distance.pdist(test_array_1, 'euclidean')
        make_square = distance.squareform(calculate_distances)

        for i in range(0,result_array.shape[1]):
            # print(result_array[i,i])
            self.assertEqual(result_array[i,i], 0)

        for i in range(0,make_square.shape[1]):
            # print(make_square[i,i])
            self.assertEqual(make_square[i,i], 0)



    def test_003_adjacency_matrix_ok(self):
        """
        Tests to ensure that adjacency matrix prepared correctly
        To show that distance.pdist function calculates correctly on a pdb.cif file
        """

        print("Test Three... To show that distance.pdist function calculates correctly on a pdb.cif file")

        with open('./extracted_test_data/1j5a.cif') as infile:
            target_list = infile.read().split('\n')
            df_1 = pd.DataFrame(data=target_list, columns=["header"])  # Put list in a dataframe m X 1 column
            df_1 = df_1[:-1] # Removes additional row that is included
            cif_to_df_2 = df_1.header.str.split(expand=True)  # Put dataframe to m x 20 columns
            critical_info_to_df_3 = cif_to_df_2.drop(columns=[0, 1, 2, 3, 4, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20], axis=1)  # df containing aa & coordinate positions
            print(critical_info_to_df_3.head())
            convert_to_array = critical_info_to_df_3.drop(columns=[5], axis=1).to_numpy() # Removes aa flag & contains only coordinate info
            calculate_distances = distance.pdist(convert_to_array, 'euclidean')
            make_square = distance.squareform(calculate_distances)
            print(make_square)

            assert df_1.shape[0] == cif_to_df_2.shape[0]
            assert cif_to_df_2.shape[0] == critical_info_to_df_3.shape[0]

    def test_004_adjacency_matrix_ok(self):
        """
        Tests to ensure that adjacency matrix prepared correctly
        To show that distance.pdist function calculates correctly on a pdb.cif file
        """

        print("Test Four... To show that distance.pdist function calculates correctly on a pdb.cif file")

        with open('./extracted_test_data/1j5a.cif') as infile:
            target_list = infile.read().split('\n')
            df_1 = pd.DataFrame(data=target_list, columns=["header"])  # Put list in a dataframe m X 1 column
            df_1 = df_1[:-1] # Removes additional row that is included
            cif_to_df_2 = df_1.header.str.split(expand=True)  # Put dataframe to m x 20 columns
            critical_info_to_df_3 = cif_to_df_2.drop(columns=[0, 1, 2, 3, 4, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20], axis=1)  # df containing aa & coordinate positions
            convert_to_array = critical_info_to_df_3.drop(columns=[5], axis=1).to_numpy() # Removes aa flag & contains only coordinate info
            calculate_distances = distance.pdist(convert_to_array, 'euclidean')
            make_square = distance.squareform(calculate_distances)

            for i in range(0,make_square.shape[1]):
                print(make_square[i,i])
                self.assertEqual(make_square[i,i], 0)


    def test_005_adjacency_matrix_ok(self):
        """
        Tests to ensure that adjacency matrix prepared correctly
        To show that adjacency matrix maintains its form when converted back into a dataframe
        """

        print("Test Five...")

        with open('./extracted_test_data/1j5a.cif') as infile:
            target_list = infile.read().split('\n')
            df_1 = pd.DataFrame(data=target_list, columns=["header"])  # Put list in a dataframe m X 1 column
            df_1 = df_1[:-1] # Removes additional row that is included
            cif_to_df_2 = df_1.header.str.split(expand=True)  # Put dataframe to m x 20 columns
            critical_info_to_df_3 = cif_to_df_2.drop(columns=[0, 1, 2, 3, 4, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20], axis=1)  # df containing aa & coordinate positions
            convert_to_array = critical_info_to_df_3.drop(columns=[5], axis=1).to_numpy() # Removes aa flag & contains only coordinate info
            calculate_distances = distance.pdist(convert_to_array, 'euclidean')
            make_square = distance.squareform(calculate_distances)
            adjacency_matrix_df_4 = pd.DataFrame(make_square)
            df_join = pd.concat([critical_info_to_df_3, adjacency_matrix_df_4], axis=1, join='inner')  # Join the databases
            df_join_2 = df_join.drop(columns=[10, 11, 12], axis=1) # Remove original coordinate information

            assert critical_info_to_df_3.shape[0] == adjacency_matrix_df_4.shape[0]
            assert adjacency_matrix_df_4.shape[0] == df_join.shape[0]
            assert df_join.shape[0] == df_join_2.shape[0]

    def test_006_adjacency_matrix_ok(self):
        """
        Tests to ensure that adjacency matrix prepared correctly
        To show that adjacency matrix maintains its form when converted back into a dataframe
        """

        print("Test Five...")

        with open('./extracted_test_data/1j5a.cif') as infile:
            target_list = infile.read().split('\n')
            df_1 = pd.DataFrame(data=target_list, columns=["header"])  # Put list in a dataframe m X 1 column
            df_1 = df_1[:-1] # Removes additional row that is included
            cif_to_df_2 = df_1.header.str.split(expand=True)  # Put dataframe to m x 20 columns
            critical_info_to_df_3 = cif_to_df_2.drop(columns=[0, 1, 2, 3, 4, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20], axis=1)  # df containing aa & coordinate positions
            convert_to_array = critical_info_to_df_3.drop(columns=[5], axis=1).to_numpy() # Removes aa flag & contains only coordinate info
            calculate_distances = distance.pdist(convert_to_array, 'euclidean')
            make_square = distance.squareform(calculate_distances)
            adjacency_matrix_df_4 = pd.DataFrame(make_square)
            print(adjacency_matrix_df_4.head())
            print(adjacency_matrix_df_4.tail())
            print(adjacency_matrix_df_4.shape)

            self.assertEqual(adjacency_matrix_df_4.shape[0], adjacency_matrix_df_4.shape[1])

            df_join = pd.concat([critical_info_to_df_3, adjacency_matrix_df_4], axis=1, join='inner')  # Join the databases
            df_join_2 = df_join.drop(columns=[10, 11, 12], axis=1) # Remove original coordinate information
            print(df_join_2.head())
            print(df_join_2.shape)



            # df_join_2.to_csv('./' + self.walk_path + '/adjacency_matrix_' + name.split('.')[0] + '.csv', encoding='utf-8', index=False, header=False)

















# data = {0:["ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY", "HIS", "ILE", "LEU",
        #            "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL"],
        #         'CID':[5950, 6322, 6267, 5960, 5862, 5961, 33032, 750, 6274, 6306, 6106, 5962,
        #                6137, 6140, 614, 5951, 6288, 6305, 6057, 6287]}
        # amino_acids_df = pd.DataFrame.from_dict(data)
        # amino_acids_df.rename(columns={0:'amino_acid_label'}, inplace=True)
        # standardised_features_df = pd.read_csv('../standardised_features.csv')
        #
        #
        # adjacency_matrix_df = pd.read_csv('./adjacency/adjacency_matrix_1tew.csv', header=None)
        # adjacency_matrix_df.rename(columns={0:'amino_acid_label'}, inplace=True)
        # adjacency_matrix_df.drop(columns=['amino_acid_label'], axis=1, inplace=True)
        #
        # protein_tags_df = pd.DataFrame(data=adjacency_matrix_df['amino_acid_label'])
        # merge_amino_acids_and_features = pd.merge(self.amino_acids_df, self.standardised_features_df, on='CID', how='left')  # Join the databases
        # merge_amino_acids_and_features.drop(columns=['CID'], axis=1, inplace=True) # Remove potential duplicate columns for next step
        # merge_features_and_protein_tag = pd.merge(protein_tags_df, merge_amino_acids_and_features, on='amino_acid_label', how='left')  # Join the databases
        #
        # self.assertEquals(adjacency_matrix_df.shape[0], adjacency_matrix_df.shape[1])



        # Convert to numpy arrays, pytorch tensor & save numpy & pickle

        # Adjacency matrix
        # adjacency_to_array = adjacency_matrix_df.drop(columns=['amino_acid_label'], axis=1).to_numpy() # Convert to numpy array
        # adjacency_to_tensor = torch.from_numpy(adjacency_to_array) # Convert to pytorch tensor
        # with open('./' + self.walk_path + '/' + name.split('_')[2].split('.')[0] + '_label', 'wb') as file:
        #     pickle.dump(adjacency_to_tensor, file) # Save as a pickle object
        # np.save('./' + self.walk_path + '/' + name.split('_')[2].split('.')[0] + '_adjacency', adjacency_to_array) # Save numpy array
        #
        #
        # # Amino acid labels
        # protein_tag_to_array = protein_tags_df.to_numpy()
        # np.save('./' + self.walk_path + '/' + name.split('_')[2].split('.')[0] + '_amino_acid_tag', protein_tag_to_array)
        #
        # # Amino acid features
        # features_to_array = merge_features_and_protein_tag.drop(columns=['amino_acid_label'], axis=1).to_numpy()
        # features_to_tensor = torch.from_numpy(features_to_array) # Convert to pytorch tensor
        # with open('./' + self.walk_path + '/' + name.split('_')[2].split('.')[0] + '_feature', 'wb') as file:
        #     pickle.dump(features_to_tensor, file) # Save as a pickle object
        # np.save('./' + self.walk_path + '/' + name.split('_')[2].split('.')[0] + '_features', features_to_array)



