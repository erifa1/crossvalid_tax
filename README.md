# crossvalid_tax
This program compares affiliations of the same sequences from metaxa2 and sintax with the same reference database. If there is ambiguity, we choose the sintax affiliation and add [amb] as prefix.

# Help
./crossvalid_tax.py -h

# Usage
./crossvalid_tax.py -s out.sintax -m out_metaxa2.taxonomy.txt
