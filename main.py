from argparse import ArgumentParser
from laststructures import get_last_load_query, get_obsoletes
from report import print_detailed_report
from rna import contains_RNA_chains
from structuresstatus import get_obsoletes_for, get_supersedings_for

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-a", "--all", action="store_true", help="process entire list of obsolete structures")
    args = parser.parse_args()

    structures_pairs = []

    if not args.all:
        supersedings = get_last_load_query()
        structures_pairs = get_obsoletes_for(supersedings)
    else:
        obsoletes = get_obsoletes()
        structures_pairs = get_supersedings_for(obsoletes)
    
    structures_pairs = [(obsolete, superseding) for obsolete, superseding in structures_pairs if contains_RNA_chains(obsolete) and contains_RNA_chains(superseding)]

    if len(structures_pairs) == 0:
        print("There are no superseded structures which contains RNA chains")
        quit()
    
    print_detailed_report(structures_pairs)
