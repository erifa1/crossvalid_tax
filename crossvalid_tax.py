#!/usr/bin/env python3

#./crossvalid_tax.py -s out.sintax -m out_metaxa2.taxonomy.txt

import argparse, sys

def main ():
    options = _set_options()
    sys.stdout = open(options.outname,'wt')
    _crossvalid_tax(options)

def _crossvalid_tax (options):

    filin1 = open(options.input1,"r") #input and sort
    filsort1= sorted(filin1)

    filin2 = open(options.input2,"r")
    filsort2= sorted(filin2)

    fil3 = filsort1 + filsort2
    print("SeqID\tcrossvalidated_tax") #output header
    for x in range(0, len(filsort1)):

        li1 = filsort1[x].rstrip("\n").split(sep='\t') #suppress \n and convert in list
        li2 = filsort2[x].rstrip("\n").split(sep='\t')

        id1 = li1[0]
        tax1 = li1[3].split(sep=',')        #adjust field (depending on seq IDs)
        tax1.extend(("NA","NA","NA","NA","NA","NA"))    #prevent affiliation with less than 7 ranks
        tax2 = li2[1].split(sep=';')
        
        tax2.extend(("NA","NA","NA","NA","NA","NA"))    

        taxf = []
        gg=["k__","p__","c__","o__","f__","g__","s__"]
        for rank in range(0,7):
            if tax1[rank][2:]==tax2[rank]:
                rankf=gg[rank]+tax2[rank]
                #print(rankf)
                taxf.append(rankf)
            else:
                rankf2=gg[rank]+tax1[rank][2:]
                #print(rankf2)
                taxf.append("[amb]"+rankf2)
        out1 = ';'.join(taxf)
        
        out2 = []
        out2.append(id1)
        out2.append(out1)
        
        outf = '\t'.join(out2)
        print(outf)

def _set_options ():
    parser = argparse.ArgumentParser(description='This program compares affiliations of the same sequences from metaxa2 and sintax with the same reference database. If there is ambiguity, we choose the sintax affiliation and add [amb] as prefix.')
    parser.add_argument('-s','--i-sintax-taxtable',action='store',required=True,type=str,dest='input1',help='Sintax output.')
    parser.add_argument('-m','--i-metaxa-taxtable',action='store',required=True,type=str,dest='input2',help='Metaxa output.')
    parser.add_argument('-o','--output_name',action='store',default="crossvalid_output.txt",type=str,dest='outname',help='Output file name. The output file is tabulated.') #si default=0 affiche le resultats dans la console.
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()