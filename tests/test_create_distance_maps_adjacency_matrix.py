#!/usr/bin/env python

"""Tests for `create_distance_maps_adjacency_matrix` package."""

import os
import unittest
from structure_prediction import create_adjacency_matrix


class TestCreate(unittest.TestCase):
    """Tests for `create_distance_maps_adjacency_matrix` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_001_create_distance_ok(self):
        """
        Test that shape of dataframes is maintained during the different manipulations
        """
        cif_names = ['11bg.cif', '123l.cif']
        walk_path = 'tests/test_data'

        create_adjacency_matrix(cif_names)

    #     pubchem_api.ApiGetFeatures(base_url, compound_cid_selector, search_id, property, output_property, output_format, output_file_name)
    #
    #     with open(output_file_name+".txt", "r") as f:
    #         contents = f.read()
    #         assert(contents == "status code is 200.")
    #
    #     os.remove(output_file_name+".txt")
    #     os.remove(output_file_name+".csv")
    #
    # # def test_002_mock_is_ok(self):
    # #     """Mock testing"""
    # #     base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/"
    # #     compound_cid_selector = "compound/cid/"
    # #     search_id = "6322/"
    # #     property = "property/"
    # #     output_property = "MolecularWeight/"
    # #     output_format = "CSV"
    # #     output_file_name = "test_data"
    # #     with mock.patch('requests.get') as mocker:
    # #         resp_mock = mock.NonCallableMagicMock(spec_set = requests.Response())
    # #         resp_mock.url  = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6322/property/MolecularWeight/CSV'
    # #         resp_mock.status_code = 200
    # #         mocker.return_value = resp_mock
    # #
    # #         resp = requests.get(pubchem_api.ApiGetFeatures(base_url, compound_cid_selector, search_id, property, output_property, output_format, output_file_name))
    # #
    # #         assert resp.status_code == 200
    # #         assert resp.url == 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6322/property/MolecularWeight/CSV'
    # #         assert mocker.called
    #
    # def test_command_line_interface(self):
    #     """Test the CLI."""
    #     runner = CliRunner()
    #     result = runner.invoke(cli.main)
    #     assert result.exit_code == 0
    #     assert 'pubchem_api.cli.main' in result.output
    #     help_result = runner.invoke(cli.main, ['--help'])
    #     assert help_result.exit_code == 0
    #     assert '--help  Show this message and exit.' in help_result.output
