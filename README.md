# scan_gvf_rsID
Python script to scan the bos_taurus.gvf file to fetch base pair position, chromosome number, alleles for a list of rsIDs

Download the bos_taurus.gvf.tz file from Ensembl. Decompress it.
Make an input file containing rsIDs for which you want base pair position, chromosome number, reference allele and alternate allele.
Input file should contain one rsID per row.
Modify the python script. Give path to your input file and bos_taurus.gvf file in the script.
The script will run with the command python3 script_name.py inputfile.txt bos_taurus.gvf
