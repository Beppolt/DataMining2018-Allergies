# DataMining2018-Allergies
This repository contais all the codes, data and results of our project for the Master course of Biological Data Mining (UniTN).
<p align="center">
  <img width="225" height="225" src="https://upload.wikimedia.org/wikipedia/it/thumb/e/e4/Sigillo_Universit%C3%A0_di_Trento.svg/150px-Sigillo_Universit%C3%A0_di_Trento.svg.png">
</p>

# Abstract

Allergies are pathological conditions caused by the response of the immune system to typically harmless substances in the environment. Corticosteroids are highly effective drugs for allergies. They can reduce the inflammation, and treat all the annoying symptoms such as  nasal stuffiness, sneezing, and itchy. However, the side effect of this corticoid therapies can lead to severe conditions which may include hormonal changes in the case of long-term use.
We developed an approach based on the analysis of the correlation between the gene expression of targets involved with allergies. We leaned on a new software, Nesra, to obtain the lists of correlated genes with the ones targeted by allergies drug, including the cortisone. 
We constructed a mapping table with the target genes and their expanded lists, and through unsupervised learning method  we seek for the genes which may have an involvement in the pathway of the corticosteroid-responsive genes. This preliminary work is a promising approach to investigate the correlations among genes and to hypothesize a replacement for the corticosteroid drug.

<p align="center">
  <img src="Cortisone.png">
</p>

# Report

In order to get more info about our studies and see the details of our workload, you can freely access our report from the following URL: 

# Source code

- **best500.py**: sort the reduced map table based on the number of target gene with non-zero relative frequencies in the descending order, then select the best 500 genes to study.
- **compact_iso_minimum.py**: compact isoforms of target genes, taking the lowest value when genes in expansion lists have more than one non-zero relative frequency. 
- **compact_rows_maximum.py**: compact isoforms of genes in expansion lists, taking the highest value when a non-zero relative frequency appears for multiple target genes.
- **map_table.py**: given as input the expansion lists and a threshold value, discard genes in expansion lists with relative frequency lower than the threshold, than build a Python Dataframe containing our target genes as columns, genes in lists s row and relative frequencies inside cells.
- **Mapping_table_analysis.R**: collection of algorithms used to analyze the map table (clustering, PCA, etc.)
- **script_targets.ipynb**: given as input the targets genes we needed to expand using NESSRA, it returns as output the file to send in order to start the expansion pipeline.
- **searchfiles.ipynb**: read csv file (gene@home table) and make a dictionary where key is t123456 code and value is its name, then look for t123456 name in dict and return its id in the gene@home table, storing mapping id-name (in T123456 syntax) on csv file. Last call rclone command to move files from experiments_result folder to our folder.


# Team members

- Giulia Marianini
- Martina Paganin
- Stefania Pirrotta
- Giuseppe Spallitta


