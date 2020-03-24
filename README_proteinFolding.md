# Intro & Set-Up

### Command line tools for downloading the protein data base (PDB) dataset

See:
- http://www.wwpdb.org/ftp/pdb-ftp-sites

To download coordinate files in PDB Exchange Format using the macromolecular Crystallographic Information File (mmCIF) run the following commands:


```bash

rsync -rlpt -v -z --delete --port=33444 \
rsync.rcsb.org::ftp_data/structures/divided/mmCIF/ ./mmCIF
```
Downloading the entire PDB data base will take approx 2 1/2 days & will require 43.94 GB of disk space.

### Data Items Describing Atomic Positions

See:
- http://mmcif.wwpdb.org/docs/tutorials/content/atomic-description.html

### Data Items Describing Molecular Entities

See:
- http://mmcif.wwpdb.org/docs/tutorials/content/molecular-entities.html

### Introduction to PDB Format

See:
- https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html

### Preprocessing the data

Once the database has been downloaded, it must be unzipped and all files must reside in the same location. I couldn't find an easy way to do this so I wrote two bash scripts that perform these tasks. They are run from the ```preProcessing.py``` script in the ```src``` folder.

The ```preProcessing.py``` file prepares one numpy array per Protein Data Base entry which is the precursor to building distance heatmaps for $\alpha$-Carbon atoms.  

It is important to specify your paths to data folders in the ```destinationVariables.py``` file, also in the ```src``` folder. Three data folders are required:

- one containing the original data downloaded from the Protein Data Bank (here ```proteinDataBase```)
- one to receive the entries that are DNA or RNA sequences and NOT protein sequenbces(here ```dna_rna```)<sup>*</sup>
- and one folder to contain the arrays that are generated by the script (here ```arrays```)

Each variable specifies the path to the data folder. It is also **very important** to specify the correct paths to the data files in the bash files. **Very Important**.



<sup>*</sup> <span style='font-size:0.7rem;'> It is important to remove the entries containing DNA or RNA 3D structure as they do not have the same format as protein 3D files. This leads to errors when trying to manipulate the numpy arrays</span>

The ouput of the ```preProcessing.py``` file is a collection of numpy arrays, one for each protein entry. The array (matrix) contains the following information:

- $\alpha$-Carbon
- Amino Acid 3-letter code
- x-coordinate of the $\alpha$-Carbon
- y-coordinate of the $\alpha$-Carbon
- z-coordinate of the $\alpha$-Carbon

In subsequent data processing steps, the column for the $\alpha$-Carbon should be deleted & the amino acid one-hot encoded.

For the preparation of distance heatmaps, both the $\alpha$-Carbon column & the amino acide column should be removed before processing the file.